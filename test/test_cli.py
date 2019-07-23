import unittest
from test.test_case import TestCase
from tr_cli.cli import Cli


class TestCli(TestCase):
    _cli = None

    def setUp(self) -> None:
        super().setUp()

        self._mock_yaml.load.return_value = {'auth': {
            'user_id': 'user_id',
            'token': 'token'
        }}

        self._cli = self._factory.secure(Cli)

    def test_arbitrary_post(self):
        self._cli.run("post", "endpoint")

        self._mock_api.post.assert_any_call("endpoint")

    def test_authenticates_api(self):
        self._mock_api.authenticate.assert_any_call("user_id", "token")

    def test_loads_config(self):
        self._mock_yaml.load.assert_any_call('config.yaml')

    def test_returns_api_response(self):
        self._mock_api.post.return_value = 'response'

        result = self._cli.run("post", "endpoint")

        self.assertEqual('response', result)


if __name__ == '__main__':
    unittest.main()
