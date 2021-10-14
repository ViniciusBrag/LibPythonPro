from unittest.mock import Mock
from LibPythonPro import github_api

def teste_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'ViniciusBrag', 'id': 87455091,
        'avatar_url': 'https://avatars.githubusercontent.com/u/87455091?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('ViniciusBrag')
    assert 'https://avatars.githubusercontent.com/u/87455091?v=4' == url