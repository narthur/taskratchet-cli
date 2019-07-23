import unittest
from unittest.mock import MagicMock
from natlibpy.factory import Factory
from tr_cli.api import Api
from tr_cli.yaml import Yaml


class TestCase(unittest.TestCase):
    _factory = None

    _mock_api = None
    _mock_yaml = None

    def setUp(self) -> None:
        super().setUp()

        self._factory = Factory()

        self._mock_api = self.__mock(Api)
        self._mock_yaml = self.__mock(Yaml)

    def __mock(self, class_):
        mock = MagicMock(spec_set=class_)

        self._factory.inject(mock)

        return mock
