from ad_api.base import ApiResponse, BaseClient
from ad_api.base.helpers import endpoint


class keyword_suggestions(BaseClient):

    @endpoint('/api/v1/keyword_suggestions', method='GET')
    def keyword_suggestions(self, adGroupId, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), params=kwargs.update({"adGroupId": adGroupId}))
