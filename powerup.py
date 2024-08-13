import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 2.0

# PASSO 1 - ABRIR O NAVEGADOR CHROME

pyautogui.press('win')
pyautogui.write('chrome')
time.sleep(2)
pyautogui.press('enter')
time.sleep(3)

# PASSO 2 - ENTRAR NO LINK ABAIXO

pyautogui.press('f6')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(5)

# PASSO 3 - FAZER LOGIN

# login
pyautogui.click(460,471)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write('pedrohenrique')
pyautogui.press('tab')

# senha
pyautogui.write('pedrohenrique')
# logar
pyautogui.click(788,665)

#PASSO 4 - IMPORTAR BASE DE DADOS

tabela = pd.read_csv('produtos.csv')

print(tabela)

#PASSO 5 - CADASTRAR PRODUTO

# repetir em todos os espaços ate finalizar informações da tabela
for linha in tabela.index: 

    #CODIGO
    codigo = str(tabela.loc[linha, 'codigo']) #transformar em texto str  
    pyautogui.click(460,325)
    pyautogui.write(codigo)
    

    #MARCA
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    pyautogui.write(marca)
    

    #TIPO
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    pyautogui.write(tipo)
    

    #CATEGORIA
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.press('tab')
    pyautogui.write(categoria)
    

    #PRECO_UNITARIO
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.press('tab')
    pyautogui.write(preco_unitario)
    
    #CUSTO
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.press('tab')
    pyautogui.write(custo)

    #OBS
    pyautogui.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)

    #clicar em cadastrar
    pyautogui.press('tab')
    pyautogui.press('enter')

    #rolar pagina para o inicio acima
    pyautogui.press('home')

    
