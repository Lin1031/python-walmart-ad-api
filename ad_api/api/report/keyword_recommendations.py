from ad_api.base import ApiResponse, BaseClient
from ad_api.base.helpers import endpoint


class ItemRecommendations(BaseClient):

    @endpoint('/api/v1/snapshot/recommendations', method='POST')
    def create_keyword_recommendations(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), json=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/snapshot', method='GET')
    def list_keyword_recommendations(self, data, **kwargs) -> ApiResponse:
        # data = {"advertiserId" : advertiserId, "snapshotId" :snapshotId}
        return self._request(kwargs.pop('path'), params=kwargs.update(data))
