from unittest.mock import Mock

from LibPythonPro.spam.main import EnviadorSpam
from LibPythonPro.spam.models import Usuario
from LibPythonPro.spam.sent_email import Sent
from LibPythonPro.tests.test_spam.confteste import *



@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Vinicius', email='Vbragadev@gmail.com'),
            Usuario(nome='Renzo', email='Vbragadev@gmail.com')
        ],
        [
            Usuario(nome='Vinicius', email='Vbragadev@gmail.com')
        ]
   ]
)
def test_qde_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'Vbragadev@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count

def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Vinicius', email='Vbragadev@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'Vbragadev@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'Vbragadev@gmail.com',
        'Vbragadev@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )

