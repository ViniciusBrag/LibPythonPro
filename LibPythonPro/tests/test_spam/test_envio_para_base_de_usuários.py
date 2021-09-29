from LibPythonPro.spam.main import EnviadorSpam
from LibPythonPro.spam.sent_email import Sent
from LibPythonPro.tests.test_spam.confteste import *



def test_qde_spam(sessao):
    enviador_de_spam = EnviadorSpam(sessao, Sent())
    enviador_de_spam.enviar_emails(
        'Vbragadev@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )


