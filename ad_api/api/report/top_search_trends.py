from ad_api.base import ApiResponse, BaseClient
from ad_api.base.helpers import endpoint


class TopSearchTrends(BaseClient):

    @endpoint('/api/v1/insights', method='GET')
    def list_top_search_trends(self, **kwargs) -> ApiResponse:
        data = {"insightsType": "searchTrends", "format": "gzip"}
        return self._request(kwargs.pop('path'), params=kwargs.update(data))
