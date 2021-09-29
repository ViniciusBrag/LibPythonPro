import pytest

from LibPythonPro.spam.data_base import Conexao


@pytest.fixture(scope='session')
def conexao():
    # Na função que foi parametrizado(conexao).A fixture vai buscar a função que tem o mesmo nome se houver,
    # e vai produzir o objeto do tipo conexão , ou seja ai reproduzir a Classe de mesmo nome , que se encontra em
    # LibPythonPro.spam.data_base
    # Setup
    conexao_obj = Conexao()
    yield conexao_obj
    # Tear Down
    conexao_obj.fechar()


@pytest.fixture()
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()


