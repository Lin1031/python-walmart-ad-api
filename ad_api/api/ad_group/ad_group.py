from ad_api.base import ApiResponse, BaseClient
from ad_api.base.helpers import endpoint


class AdGroups(BaseClient):

    @endpoint('/api/v1/adGroups', method='POST')
    def create_ad_groups(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/adGroups', method='PUT')
    def edit_ad_groups(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/adGroups', method='GET')
    def list_ad_groups(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)