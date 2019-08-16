import requests


class Api:
    _user_id = None
    _token = None
    # _url = 'https://us-central1-taskratchet.cloudfunctions.net/api1/'
    _url = 'https://us-central1-taskratchet.cloudfunctions.net/staging/'

    def authenticate(self, user_id, token):
        self._user_id = user_id
        self._token = token

    def post(self, endpoint):
        api_endpoint = self._url + endpoint

        print(api_endpoint)

        return requests.post(
            api_endpoint,
            data={
                'user_id': self._user_id,
                'token': self._token
            }
        )

    def get(self, endpoint):
        api_endpoint = self._url + endpoint

        print(api_endpoint)

        return requests.get(
            api_endpoint,
            headers={
                'X-Taskratchet-Userid': str(self._user_id),
                'X-Taskratchet-Token': str(self._token)
            }
        )
