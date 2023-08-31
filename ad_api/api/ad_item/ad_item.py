from ad_api.base import ApiResponse, BaseClient
from ad_api.base.helpers import endpoint


class AdItems(BaseClient):

    @endpoint('/api/v1/adItems', method='POST')
    def create_ad_items(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), json=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/adItems', method='PUT')
    def edit_ad_items(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), json=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/adItems', method='GET')
    def list_ad_items(self, campaignId, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), params=kwargs.update({"campaignId": campaignId}))
