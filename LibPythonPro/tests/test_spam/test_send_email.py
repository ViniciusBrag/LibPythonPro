import pytest

from LibPythonPro.spam.sent_email import Sent, EmailInvalido


def test_criar_send_email():
    send = Sent()
    assert send is not None


@pytest.mark.parametrize(
    'remetente',
    ['Vbragadev@gmail.com', 'foo@bar.com.br']
)
def test_remetente(remetente):
    send = Sent()
    resultado = send.enviar(
        remetente,
        'luciano@python.pro.br',
        'Cursos Python Pro!',
        'Primeira turma Guido Von Rossum aberta'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    [' ', 'Vbragadev']
)
def test_remetente_invalido(remetente):
    send = Sent()
    with pytest.raises(EmailInvalido):
        send.enviar(
            remetente,
            'luciano@python.pro.br',
            'Cursos Python Pro!',
            'Primeira turma Guido Von Rossum aberta'
        )
