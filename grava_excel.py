# coding: utf-8


"""

Módulo grava_excel.py: Módulo responsável por performar atividades de
abertura, gravação e salvamento de planilhas Excel.

"""

import xlsxwriter as xw
import os


class PlanDados:
    """

    Classe principal pdo módulo, incorporandos os principais métodos
    utilizados para tratamento da planilha de dados Excel.

    """

    def __init__(self):
        """Método construtor responsável por inicializar as variáveis de
        ambiente para execução
        """
        self.save_path = 'dados_vagas.xlsx'

        # Configurar planilha de dados
        self.linha = 1
        self.workbook = xw.Workbook(self.save_path)
        self.worksheet = self.workbook.add_worksheet()

        # Gravar cabeçalhos
        self.worksheet.write(0, 0, 'Nome')
        self.worksheet.write(0, 1, 'Local')
        self.worksheet.write(0, 2, 'Descrição')


    def gravar_vaga(self, *args):
        """Método responsável por gravar os dados da vaga na planilha

        :param args: Nome, Local e Descrição da vaga
        :return: None
        """
        nome, local, descricao = args

        # Gravar daods
        self.worksheet.write(self.linha, 0, nome)
        self.worksheet.write(self.linha, 1, local)
        self.worksheet.write(self.linha, 2, descricao)

        # Incrementa lina
        self.linha += 1

    def salvar_plan(self):
        """Método responsável por fechar e salvar a planilha de dados.

        :return: None
        """
        try:
            # Remove arquivo antigo se houver
            os.remove(self.save_path)
        except FileNotFoundError:
            pass
        finally:
            # Salva e fecha a planilha
            self.workbook.close()