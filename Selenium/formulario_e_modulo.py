from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import dados as D

driver = webdriver.Chrome()

try:
    # Acessando o site teste de formulário
    driver.get("https://www.input.com.vc/teste-formulario/")
    sleep(3)

    # Preenchendo dados pessoais
    driver.find_element(By.NAME, 'nome').send_keys(D.nome_completo)
    driver.find_element(By.NAME, 'sexo').click()
    driver.find_element(By.NAME, 'CPF').send_keys(D.cpf)
    driver.find_element(By.NAME, 'nascimento').send_keys(D.nascimento)
    driver.find_element(By.NAME, 'RG').send_keys(D.rg)
    driver.find_element(By.NAME, 'uf-RG').send_keys(D.uf)
    driver.find_element(By.NAME, 'expeditor-RG').send_keys(D.orgao_rg)
    driver.find_element(By.NAME, 'pai').send_keys(D.nome_pai)
    driver.find_element(By.NAME, 'mae').send_keys(D.nome_mae)
    driver.find_element(By.NAME, 'profissao-pai').send_keys(D.prof_pai)
    driver.find_element(By.NAME, 'profissao-mae').send_keys(D.prof_mae)

    # Transporte
    driver.find_element(By.NAME, 'checktransporte').click()

    # Endereço
    driver.find_element(By.NAME, 'CEP').send_keys(D.cep)
    driver.find_element(By.NAME, 'endereco').send_keys(D.logadouro)
    driver.find_element(By.NAME, 'bairro').send_keys(D.bairro)
    driver.find_element(By.NAME, 'cidade').send_keys(D.cidade)
    driver.find_element(By.NAME, 'UF').send_keys(D.uf)

    # Contador
    driver.find_element(By.NAME, 'fone').send_keys(D.tel_res)
    driver.find_element(By.NAME, 'celular').send_keys(D.tel_cel)
    driver.find_element(By.NAME, 'correio').send_keys(D.e_mail)
    driver.find_element(By.NAME, 'facebook').send_keys(D.facebook)
    driver.find_element(By.NAME, 'linkedin').send_keys(D.linkedin)
    driver.find_element(By.NAME, 'Instagram').send_keys(D.intagram)

    # Profissional
    driver.find_element(By.NAME, 'cargo-1').send_keys(D.cargo)
    driver.find_element(By.NAME, 'salario-1').send_keys(D.salario)
    driver.find_element(By.NAME, 'id:beneficios').send_keys(D.beneficio)
    driver.find_element(By.NAME, 'periodo1').send_keys(D.pr_ini)
    driver.find_element(By.NAME, 'periodo1-b').send_keys(D.pr_fim)
    driver.find_element(By.NAME, 'Atividades').send_keys(D.atividades)

    # Anexando os arquivos
    driver.find_element(By.NAME, 'foto').send_keys(
        r'C:\Users\phlis\OneDrive\Área de Trabalho\PROJETO TESTE - SELENIUM - PYAUTOGUI\Selenium\download.jpg')
    driver.find_element(By.NAME, 'CV').send_keys(
        r'C:\Users\phlis\OneDrive\Área de Trabalho\PROJETO TESTE - SELENIUM - PYAUTOGUI\Selenium\CV - Pedro Lisboa.pdf')

    # Enviando
    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[2]/form/div[40]/input').click()

    # Finanlizando o navegador
    sleep(15)
    driver.quit()

except Exception as e:
    print(f'Error {e}')
