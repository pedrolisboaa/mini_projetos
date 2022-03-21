import pymysql.cursors

teste_tupla = ('GLADSON DE LIMA CAMELI   [2019]', 'Rio Branco   [2010]', 'acriano', '164.173,431 km²   [2021]',
               '906.876 pessoas   [2021]', '4,47 hab/km²   [2010]', '156.679 matrículas   [2020]', '0,663   [2010]',
               '6.632.883,11 R$ (×1000)   [2017]', '6.084.416,81 R$ (×1000)   [2017]', '888 R$   [2021]',
               '306.258 veículos   [2020]')


class EstadosDados:
    def __init__(self):
        self.conexao = pymysql.connect(host='127.0.0.1',
                                       user='root',
                                       password='',
                                       db='cidades_brasileiras',
                                       charset='utf8mb4',
                                       cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conexao.cursor()

    def inserir_dados(self, dados):
        sql = "INSERT INTO informacoes (GOVERNADOR, CAPITAL, GENTILICO, AREA_TERRITORIAL, POPULACAO_ESTIMADA, " \
              "DENSIDADE_DEMOGRAFICA, MATRICULAS_NO_ENSINO_FUNDAMENTAL, IDH_INDICE_DE_DESENVOLVIMENTO_HUMANO, " \
              "RECEITAS_REALIZADAS, DESPESAS_EMPENHADAS, RENDIMENTO_MENSAL_DOMICILIAR_PER_CAPITA, TOTAL_DE_VEICULOS) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
        self.cursor.execute(sql, dados)
        self.conexao.commit()
