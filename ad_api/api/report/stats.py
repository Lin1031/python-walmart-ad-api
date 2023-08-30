from ad_api.base import ApiResponse, BaseClient
from ad_api.base.helpers import endpoint


class Stats(BaseClient):

    @endpoint('/api/v1/stats', method='GET')
    def list_stats(self, data, **kwargs) -> ApiResponse:
        # data = {"advertiserId" : advertiserId, "campaignId" :campaignId}
        return self._request(kwargs.pop('path'), params=kwargs.update(data))
