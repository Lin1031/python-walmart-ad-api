from ad_api.base import ApiResponse, BaseClient
from ad_api.base.helpers import endpoint


class Campaigns(BaseClient):

    @endpoint('/api/v1/campaigns', method='POST')
    def create_campaigns(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), json=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/campaigns', method='PUT')
    def edit_campaigns(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), json=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/campaigns', method='GET')
    def list_campaigns(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), json=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/campaigns/delete', method='PUT')
    def delete_campaigns(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), json=kwargs.pop('body'), params=kwargs)
