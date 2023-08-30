from ad_api.base import ApiResponse, BaseClient
from ad_api.base.helpers import endpoint


class SnapshotV2(BaseClient):

    @endpoint('/api/v2/snapshot/report', method='POST')
    def create_snapshot_v2(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v2/snapshot', method='GET')
    def list_snapshot_v2(self, data, **kwargs) -> ApiResponse:
        # data = {"advertiserId" : advertiserId, "snapshotId" :snapshotId}
        return self._request(kwargs.pop('path'), params=kwargs.update(data))
