import pprint


class ApiResponse:
    def __init__(self, payload=None, nextToken=None, status_code=None, headers=None, **kwargs):
        # self.payload = payload or kwargs
        self.payload = payload
        self.headers = headers
        self.next_token = nextToken
        self.status_code = status_code

    def __str__(self):
        return pprint.pformat(self.__dict__)

    def set_next_token(self, nextToken=None):
        if nextToken:
            self.next_token = nextToken
        else:
            self.next_token = self.payload.get("NextToken", None)
        return self.next_token

    @staticmethod
    def set_rate_limit(headers: dict = None):
        try:
            return headers["x-walm-RateLimit-Limit"]
        except (AttributeError, KeyError, TypeError):
            return None
