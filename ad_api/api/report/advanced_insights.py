from ad_api.base import ApiResponse, BaseClient
from ad_api.base.helpers import endpoint


class AdvancedInsights(BaseClient):

    @endpoint('/api/v1/snapshot/insight', method='POST')
    def create_snapshot_v1(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), json=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/snapshot', method='GET')
    def list_snapshot_v1(self, data, **kwargs) -> ApiResponse:
        # data = { "snapshotId" :snapshotId}
        return self._request(kwargs.pop('path'), params=kwargs.update(data))
