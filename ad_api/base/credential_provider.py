import os
import confuse
from cachetools import Cache

from ad_api.base.config import BaseConfig


class MissingCredentials(Exception):
    """
    Credentials are missing, see the error output to find possible causes
    """
    pass


class CredentialProvider:
    credentials = None
    config_class = BaseConfig
    cache = Cache(maxsize=10)

    def __init__(self, account='default', credentials=None):
        self.account = account
        self.read_credentials = [
            self.from_env,
            self.read_config
        ]
        if credentials:
            self.credentials = self.config_class(**credentials)
            missing = self.credentials.check_config()
            if len(missing):
                raise MissingCredentials(f'The following configuration parameters are missing: {missing}')
        else:
            self.load_credentials()

    def load_credentials(self):
        for read_method in self.read_credentials:
            if read_method():
                return True

    def from_env(self):
        account_data = dict(
            client_id=self._get_env('AD_API_CLIENT_ID'),
            client_secret=self._get_env('AD_API_CLIENT_SECRET'),
            consumer_id=self._get_env('AD_API_CONSUMER_ID')
        )
        self.credentials = self.config_class(**account_data)
        return len(self.credentials.check_config()) == 0

    def _get_env(self, key):
        return os.environ.get(f'{key}_{self.account}',
                              os.environ.get(key))

    def read_config(self):
        try:
            config = confuse.Configuration('python-ad-api')
            config_filename = os.path.join(config.config_dir(), 'credentials.yml')
            config.set_file(config_filename)
            account_data = config[self.account].get()
            self.credentials = self.config_class(**account_data)
            missing = self.credentials.check_config()
            if len(missing):
                raise MissingCredentials(f'The following configuration parameters are missing: {missing}')
        except confuse.exceptions.NotFoundError:
            raise MissingCredentials(f'The account {self.account} was not setup in your configuration file.')
        except confuse.exceptions.ConfigReadError:
            raise MissingCredentials(
                f'Neither environment variables nor a config file were found. '
                f'Please set the correct variables, or use a config file (credentials.yml). '
                f'See https://confuse.readthedocs.io/en/latest/usage.html#search-paths for search paths.'
            )
        else:
            return True
