# coding: utf-8


"""

Módulo envia_email.py: Módulo responsável pelo envio de e-mail contendo a
planilha de dados em anexo.

"""


import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


class EmailSender:
    """

    Classe principal do módulo. Responsável pelo envio de email ao gerente.

    """

    def __init__(self, host, port, username, password):
        """ Construtor da classe. Inicializa as variáveis de ambiente.

        :param host: Servidor SMTP
        :param port: Porta no servidor SMPT
        :param username: Usuário da e-mail que enviará a mensagem
        :param password: Senha do usuário que enviará a mensagem
        """
        self.server = smtplib.SMTP_SSL(host, port)
        self.server.login(username, password)

    def envia_email(self, email_from, email_subject, email_to, message, path):
        """Método responsável pelo envio de email

        :param email_from: Remetente do e-mail
        :param email_subject: Assunto do e-mail
        :param email_to: Destinatário do e-mail
        :param message: Mensagem que será enviada no corpor do e-mail
        :param path: Anexo do e-mail
        :return: None
        """

        # Configura objeto da mensagem com os parâmetros de entrada
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = email_to
        msg['Subject'] = email_subject
        msg.attach(MIMEText(message))

        # Lê anexo e anexa a mensagem
        part = MIMEBase('application', "octet-stream")
        with open(path, 'rb') as file:
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(Path(path).name))
            msg.attach(part)

        # Envia o e-mail e fecha a conexão
        self.server.sendmail(email_from, email_to, msg.as_string())
        self.server.quit()