import os
from redis import StrictRedis

redis_url = os.environ.get('AD_API_REDIS_URL')
if not redis_url:
    raise Exception("redis url %r not invalid" % redis_url)
redis_cache = StrictRedis.from_url(redis_url)

private_key_path = "./WM_IO_private_key.pem"



# 'redis://192.168.0.123:6379/0'
class BaseConfig:
    def __init__(self, client_id, client_secret, consumer_id):
        self.client_id = client_id
        self.client_secret = client_secret
        self.consumer_id = consumer_id

    def check_config(self):
        errors = []
        for k, v in self.__dict__.items():
            if not v and k != 'refresh_token':
                errors.append(k)
        return errors
