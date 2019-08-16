import requests


class Api:
    _user_id = None
    _token = None
    _url = 'https://us-central1-taskratchet.cloudfunctions.net'
    _v = 'api1'

    def set_staging(self, bool_):
        if bool_:
            self._v = 'staging'

    def authenticate(self, user_id, token):
        self._user_id = user_id
        self._token = token

    def post(self, endpoint):
        api_endpoint = self._expand_endpoint(endpoint)

        print(api_endpoint)

        return requests.post(
            api_endpoint,
            headers={
                'X-Taskratchet-Userid': str(self._user_id),
                'X-Taskratchet-Token': str(self._token)
            }
        )

    def get(self, endpoint):
        api_endpoint = self._expand_endpoint(endpoint)

        print(api_endpoint)

        return requests.get(
            api_endpoint,
            headers={
                'X-Taskratchet-Userid': str(self._user_id),
                'X-Taskratchet-Token': str(self._token)
            }
        )

    def _expand_endpoint(self, endpoint):
        return f'{self._url}/{self._v}/{endpoint}'
