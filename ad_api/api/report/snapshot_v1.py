from ad_api.base import ApiResponse, BaseClient
from ad_api.base.helpers import endpoint


class SnapshotV1(BaseClient):

    @endpoint('/api/v1/snapshot/report', method='POST')
    def create_snapshot_v1(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/snapshot', method='GET')
    def list_snapshot_v1(self, data, **kwargs) -> ApiResponse:
        # data = {"data" : data, "snapshotId" :snapshotId}
        return self._request(kwargs.pop('path'), params=kwargs.update(data))