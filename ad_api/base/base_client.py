import base64
import time

import requests
import hashlib

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from cryptography.hazmat.primitives import serialization
from requests import JSONDecodeError

from ad_api.base import ApiResponse
from ad_api.base.exceptions import get_exception_for_content, get_exception_for_code


class BaseClient:
    def __init__(self, consumer_id):
        self.consumer_id = consumer_id
        self.endpoint = "https://developer.api.stg.walmart.com/api-proxy/service/WPA/Api/v1"
        self.signature = None
        self.timestamp = None
        # TODO token需要调接口
        self.auth_token = ""

    def calculate_signature(self, path, params):
        self.timestamp = str(int(time.time()))
        self.signature = self.consumer_id + "\n" + self.endpoint + path + "\n" + params.get(
            'method') + "\n" + self.timestamp + "\n"

    def sign_data(self):
        try:
            with open('./WM_IO_private_key.pem', 'r') as f:
                private_key = RSA.importKey(f.read())
        except IOError as e:
            print(e)

        encoded_hash_string = self.signature.encode()
        hasher = SHA256.new(encoded_hash_string)
        signer = PKCS1_v1_5.new(private_key)
        signature = signer.sign(hasher)
        self.signature = str(base64.b64encode(signature), 'utf-8')

    @property
    def headers(self):
        return {
            "WM_CONSUMER.ID": self.consumer_id,
            "WM_SEC.TIMESTAMP": self.timestamp,
            "WM_SEC.AUTH_SIGNATURE": self.signature,
            "Content-Type": "application/json",
            "accept": "application/json"
        }

    def _request(self, path, data=None, params=None, headers=None):

        self.calculate_signature(path, params)
        self.sign_data()
        response = requests.post(self.endpoint + path, json=data, headers=headers or self.headers,
                                 params=params.update({"auth_token": self.auth_token}))

        return self._check_response(response)

    def _check_response(self, res) -> ApiResponse:

        content = vars(res).get('_content')
        str_content = content.decode('utf8')
        headers = vars(res).get('headers')
        status_code = vars(res).get('status_code')

        if 200 <= res.status_code < 300:

            try:
                js = res.json() or {}
            except JSONDecodeError:
                js = {}

            try:
                error = js.get('error', None)  # Dict.get(key, default=None)
            except AttributeError:
                error = None

            if error:
                exception = get_exception_for_content(error[0].get('code'))
                raise exception(error[0].get('code'), error[0], headers)

            next_token = vars(res).get('_next')
            return ApiResponse(js, next_token=next_token, status_code=status_code, headers=headers)

        else:

            exception = get_exception_for_code(res.status_code)
            try:
                js = res.json()
            except JSONDecodeError:
                js = res.content

            raise exception(status_code, js, headers)
            exit(res.status_code)