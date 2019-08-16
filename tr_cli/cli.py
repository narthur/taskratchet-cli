from tr_cli.api import Api
from tr_cli.yaml import Yaml


class Cli:
    _api = None
    _yaml = None

    def __init__(self, api: Api, yaml: Yaml):
        self._api = api
        self._yaml = yaml

        self._authenticate_api()

    def _authenticate_api(self):
        config = self._yaml.load('config.yaml')
        user_id = config['auth']['user_id']
        token = config['auth']['token']

        self._api.authenticate(user_id, token)

    def run(self, args):
        command = args['<method>']
        endpoint = args['<endpoint>']
        staging = args['--staging']

        self._api.set_staging(staging)

        if command == 'post':
            return self._api.post(endpoint)

        return self._api.get(endpoint)
