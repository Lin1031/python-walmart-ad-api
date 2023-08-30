import os
from redis import StrictRedis
redis_url = os.environ.get('AD_API_REDIS_URL')
if not redis_url:
    raise Exception("redis url %r not invalid" % redis_url)
redis_cache = StrictRedis.from_url(redis_url)


# 'redis://192.168.0.123:6379/0'
class BaseConfig:
    def __init__(self, refresh_token, client_id, client_secret):
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret

    def check_config(self):
        errors = []
        for k, v in self.__dict__.items():
            if not v and k != 'refresh_token':
                errors.append(k)
        return errors


class Config(BaseConfig):
    def __init__(self, refresh_token, client_id, client_secret, profile_id):
        super().__init__(refresh_token, client_id, client_secret)
        self.profile_id = profile_id
