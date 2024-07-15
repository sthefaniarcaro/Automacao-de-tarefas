# passo a passo
# passo 1 - entrar no sistema
# passo 2 - fazer login
# passo 3 - importar base de dados
# passo 4 - cadastrar produto
# passo 5 - repetir até acabar a lista de produtos

# pip install pyautogui - para uso da biblioteca
# pip install pandas openpyxl numpy

import pyautogui
import time

# pyautogui.click - clicar com o mouse
# pyautogui.write - escrever um texto
# pyautogui.press - apertar 1 tecla
# pyautogui.hotkey - combinação de teclas (como o crtl c)
# pyautogui.scroll - rolar a tela para cima ou baixo

pyautogui.PAUSE = 2 # cada pyautogui tem 0.5 seg como tempo de resposta

# PASSO 1 - entrar no sistema
# abrir o navegador
pyautogui.press("win") # botao conforme padrao do pyautogui
pyautogui.write("microsoft edge")
pyautogui.press("enter")
time.sleep(2)

# entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.click(x=427, y=49)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(4) # 3 seg como tempo de resposta + 0.5 seg do pyautogui.PAUSE (pois há um delay do navegador e etc)

# PASSO 2 - fazer login 
pyautogui.click(x=634, y=357) # posicao pega atraves do coordenadas.py - o cursor ira clicar nela
pyautogui.hotkey("ctrl", "a") # vai usar a combinacao de teclas que selecionara todo o texto e reescrevera por cima dele
pyautogui.write("automatizacao@gmail.com")

# passar para o campo de senha
pyautogui.press("tab") # para pular para o campo senha
pyautogui.write("senha")

pyautogui.click(x=683, y=516) # para validar os dados
time.sleep(3)

# PASSO 3 - importar base de dados
import pandas

tabela = pandas.read_csv("produtos.csv") # caso produtos.csv nao estivesse na mesma pasta que o codigo teria que colocar o diretório dele
print (tabela)

# PASSO 4 - cadastrar produto

# 5 - para cada linha da tabela:
for linha in tabela.index: # index está relacionado com as linhas do arquivo
    # codigo
    pyautogui.click(x=505, y=240) 
    codigo = str(tabela.loc[linha, "codigo"]) # .loc[linha, coluna] é da biblioteca pandas e transforma em string
    pyautogui.write(codigo)

    # marca 
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab") 
    pyautogui.write(marca)

    # tipo 
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab") 
    pyautogui.write(tipo)

    # categoria 
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab") 
    pyautogui.write(categoria)

    # preco_unitario 
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab") 
    pyautogui.write(preco)

    # custo 
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab") 
    pyautogui.write(custo)

    # obs
    pyautogui.press("tab") 
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan": # se obs não for vazia ela será preenchida
        pyautogui.write(obs)

    # clicar no botão de enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    # scroll para cima
    pyautogui.scroll(5000)

# PASSO 5 - repetir para todos os produtos (linhas da tabela)