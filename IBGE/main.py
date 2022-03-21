SIGLAS_ESTADOS = ['ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mt', 'ms', 'mg', 'pa', 'pb', 'pr',
                  'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc', 'sp', 'se', 'to']

from buscar import BuscarInformacoes
from dados import EstadosDados

inserir = EstadosDados()

for i in range(len(SIGLAS_ESTADOS)):
    teste = BuscarInformacoes(SIGLAS_ESTADOS[i])
    informacoes = teste.realizar_buscar()

    gambiara = []
    for i in informacoes.values():
        gambiara.append(i)

    inserir.inserir_dados(tuple(gambiara))

print('Acabou!')
