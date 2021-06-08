# coding: utf-8


"""

Módulo busca_vagas.py: Módulo responsável pela disponibilização das classes
responsáveis por buscar e tratar as vagas contidas no site da Cadmus.

"""

import requests
import json


class BuscaVagas:
    """

    Classe principal do módulo. Fornece os principais métodos da aplicação.

    """

    def __init__(self):
        """Método construtor. Inicializa as variáveis principais.
        """
        self.session = requests.session()
        self.url = 'https://apisf.cadmus.com.br/api/opportunity/listOpportunity/'
        self.list_vagas = []

    def buscar_vagas(self):
        """Busca as vagas no site da cadmus, trata e preenche a lista de vagas.
        :return: Null
        """

        # Obter vagas do portal
        self.response = self.session.get(self.url, verify=False, timeout=None)
        vagas = json.loads(self.response.content)

        # Loop de preenchimento das vagas encontradas
        for vaga in vagas:
            self.list_vagas.append(
                (
                    vaga['Name'],
                    vaga['Cidade_Regi_o__c'],
                    vaga['Descricao_da_vaga__c'].replace('</br>', '')
                )
            )
