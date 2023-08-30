from ad_api.base import ApiResponse, BaseClient
from ad_api.base.helpers import endpoint


class itemSearch(BaseClient):

    @endpoint('/api/v1/itemSearch', method='POST')
    def create_item_search(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)
