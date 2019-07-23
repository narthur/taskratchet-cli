import requests


class Api:
    _user_id = None
    _token = None

    def authenticate(self, user_id, token):
        self._user_id = user_id
        self._token = token

    def post(self, endpoint):
        api_endpoint = 'https://us-central1-taskratchet.cloudfunctions.net/api1/' + endpoint

        print(api_endpoint)

        return requests.post(
            api_endpoint,
            data={
                'user_id': self._user_id,
                'token': self._token
            }
        )
