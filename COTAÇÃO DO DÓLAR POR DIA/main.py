import requests
from datetime import datetime
import pymysql.cursors
from time import sleep

# Lidando com banco de dados
conexao = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    db='dolar',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conexao.cursor()
while True:
    # Buscando as informações na API
    cotacao_momento = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')

    for dado in cotacao_momento.json().values():
        dola_horario = (dado.get('bid'), datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        sql = 'INSERT INTO cotacao (VALOR, DATA) VALUES (%s, %s)'
        cursor.execute(sql, dola_horario)
        conexao.commit()

    print('Deu certo!')
    sleep(1800)






cursor.close()
conexao.close()

