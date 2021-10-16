from unittest.mock import Mock

import pytest

from LibPythonPro import github_api

@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/87455091?v=4'
    resp_mock.json.return_value = {
        'login': 'ViniciusBrag', 'id': 87455091,
        'avatar_url': url,
    }
    get_mock = mocker.patch('LibPythonPro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url

def teste_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('ViniciusBrag')
    assert avatar_url == url

def teste_buscar_avatar_integracao():
   url = github_api.buscar_avatar('ViniciusBrag')
   assert 'https://avatars.githubusercontent.com/u/87455091?v=4' == url
