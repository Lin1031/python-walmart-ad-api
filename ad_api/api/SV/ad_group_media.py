from ad_api.base import ApiResponse, BaseClient
from ad_api.base.helpers import endpoint


class AdGroupMedia(BaseClient):

    @endpoint('/api/v1/adGroup/media', method='POST')
    def create_group_media(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), json=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/adGroup/media', method='PUT')
    def edit_group_media(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), json=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/adGroup/media', method='GET')
    def list_group_media(self, data, **kwargs) -> ApiResponse:
        # data = {"campaignId": campaignId, "adGroupId": adGroupId}
        return self._request(kwargs.pop('path'), params=kwargs.update(data))