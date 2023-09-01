from ad_api.base import ApiResponse, BaseClient
from ad_api.base.helpers import endpoint


class SBAProfile(BaseClient):

    @endpoint('/api/v2/sba_profile', method='POST')
    def create_sba_profile(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), json=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v2/sba_profile', method='PUT')
    def edit_sba_profile(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), json=kwargs.pop('body'), params=kwargs)

    @endpoint('/api/v2/sba_profile', method='GET')
    def list_sba_profile(self, data, **kwargs) -> ApiResponse:
        # data = {"campaignId": campaignId, "adGroupId": adGroupId}
        return self._request(kwargs.pop('path'), params=kwargs.update(data))

    @endpoint('/api/v2/sba_profile_image_upload', method='PUT')
    def edit_sba_profile_image(self, data, file_path, **kwargs) -> ApiResponse:
        headers = {"Content-Type": "multipart/form-data"}
        # data='SBABaseProfileRequest ={"campaignId": "500001", "adGroupId": "500001", "sbaProfileId": "600001")'
        files = {"file": (file_path, open(file_path, "rb"), "image/png")}
        return self._request(kwargs.pop('path'), data=data, params=kwargs, headers=headers, files=files)
