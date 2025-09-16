import pyautogui # Pacote para automações em Python
import time

pyautogui.PAUSE = 2

# Passo 1: Entrar no sistema da empresa - 
# abrir o chome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.click(x=232, y=212)


time.sleep(3)

# digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Espera 3 segundos
time.sleep(5)

# Passo 2: Fazer Login
# Preencher email
pyautogui.click(x=508, y=407)
pyautogui.write("pythonimpressionador@gmail.com")

# preencher senha
pyautogui.press("tab")
pyautogui.write("minhasenhasupersecreta")

# botão logar
pyautogui.press("tab")
pyautogui.press("enter")

# Espera de 3s
time.sleep(3)

# Passo 3: Importar base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar todos os produto
for linha in tabela.index:

    pyautogui.click(x=484, y=255) 
    pyautogui.press("tab")

    codigo = str(tabela.loc[linha,"codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha,"marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha,"tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
        pyautogui.press("tab")
        pyautogui.press("enter")

    # Quando terminar o cadastro subir o scroll
    pyautogui.scroll(100000)