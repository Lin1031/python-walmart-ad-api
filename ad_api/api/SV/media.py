from ad_api.base import ApiResponse, BaseClient
from ad_api.base.helpers import endpoint, fill_query_params


class Media(BaseClient):

    @endpoint('/api/v1/adGroup/media', method='POST')
    def create_upload_media(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), json=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/media/complete', method='PUT')
    def complete_media_upload(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), json=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/media', method='PUT')
    def update_media_details(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), json=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/media', method='GET')
    def list_media(self, data, **kwargs) -> ApiResponse:
        # data = {"advertiserId": advertiserId}
        return self._request(kwargs.pop('path'), params=kwargs.update(data))

    @endpoint('/api/v1/media/{}', method='GET')
    def list_media(self, mediaId, data, **kwargs) -> ApiResponse:
        # data = {"advertiserId": advertiserId}
        return self._request(fill_query_params(kwargs.pop('path'), mediaId), params=kwargs.update(data))
