from ad_api.base import ApiResponse, BaseClient
from ad_api.base.helpers import endpoint


class Keywords(BaseClient):

    @endpoint('/api/v1/keywords', method='POST')
    def create_ad_keywords(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), json=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/keywords', method='PUT')
    def edit_ad_keywords(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), json=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/keywords', method='GET')
    def list_ad_keywords(self, campaignId, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), params=kwargs.update({"campaignId": campaignId}))
