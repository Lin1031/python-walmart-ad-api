from ad_api.base import ApiResponse, BaseClient
from ad_api.base.helpers import endpoint


class BidMultipliers(BaseClient):

    @endpoint('/api/v1/multipliers/placement', method='POST')
    def create_multipliers_placement(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/multipliers/placement', method='PUT')
    def edit_multipliers_placement(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/multipliers/placement', method='GET')
    def list_multipliers_placement(self, campaignId, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), params=kwargs.update({"campaignId": campaignId}))

    @endpoint('/api/v1/multipliers/platform', method='POST')
    def create_multipliers_platform(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/multipliers/platform', method='PUT')
    def edit_multipliers_platform(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v1/multipliers/platform', method='GET')
    def list_multipliers_platform(self, campaignId, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), params=kwargs.update({"campaignId": campaignId}))
