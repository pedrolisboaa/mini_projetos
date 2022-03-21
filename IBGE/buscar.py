import requests
import bs4


class BuscarInformacoes():
    def __init__(self, sigla):
        self.resultado = requests.get(f'https://www.ibge.gov.br/cidades-e-estados/{sigla}.html/')
        self.soup = bs4.BeautifulSoup(self.resultado.text, 'html.parser')

    def realizar_buscar(self):
        todos_dados = self.soup.findAll('p')
        dados_bonitos = []
        for dado in todos_dados:
            dado_site = dado.get_text().replace(u'\xa0', u' ')
            dados_bonitos.append(dado_site)

        # Tratando os dados e transformando em um dicionário
        del dados_bonitos[0:4]
        lista_de_chaves = []
        lista_de_valores = []

        for i, dado in enumerate(dados_bonitos):
            if i % 2 == 0:
                lista_de_chaves.append(dado)
            else:
                lista_de_valores.append(dado)

        dicionario_estado = dict(zip(lista_de_chaves, lista_de_valores))
        return dicionario_estado
