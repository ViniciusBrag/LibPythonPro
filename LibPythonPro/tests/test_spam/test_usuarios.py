from LibPythonPro.spam.models import Usuario

from LibPythonPro.tests.test_spam.confteste import *


def test_salvar_usuario(sessao):
    # setup
    usuario = Usuario(nome='Vinicius', email='Vbragadev@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)



def test_listar_usuario(conexao, sessao):
    usuarios = [
        Usuario(nome='Vinicius', email='Vbragadev@gmail.com'),
        Usuario(nome='Renzo', email='Vbragadev@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
