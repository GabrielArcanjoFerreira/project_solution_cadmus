# coding: utf-8


"""
Módulo main.py: Destina-se ao core da aplicação. A partir dele todas as demais
rotinas são executadas e gerenciadas.
"""

from busca_vagas import BuscaVagas
from grava_excel import PlanDados
from envia_email import EmailSender
import os

if __name__ == '__main__':
    """ Função que inicia toda a rotina
    """
    # Instânciar objetos
    vagas = BuscaVagas()
    plan = PlanDados()

    # Buscar vagas
    vagas.buscar_vagas()

    # Preencher no excel as vagas encontradas
    for vaga in vagas.list_vagas:
        plan.gravar_vaga(*vaga)

    # Salvar planilha
    plan.salvar_plan()

    # Enviar e-mail (preencher com variáveis de ambiente em produção)
    host = ''  # HOST SMTP
    port = None  # Porta SMTP
    username = ''  # Login da conta que enviará as mensagens
    password = ''  # Senha da conta que enviará as mensagens
    email_from = ''  # Remetente das mensagens
    email_to = ''  # Destinatário das mensagens
    email_subject = ''  # Assunto
    message = ''  # Corpo do e-mail

    """
    sender = EmailSender(host, port, username, password)
    sender.envia_email(email_from, 
                       email_subject, 
                       email_to, 
                       message, 
                       path=
                       os.path.abspath(os.getcwd()) + '\\dados_vagas.xlsx'
                       )
    """
