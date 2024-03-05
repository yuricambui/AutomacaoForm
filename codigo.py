import  pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

#abrir navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=482, y=916)

#entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2)

#efetuar login
pyautogui.click(x=820, y=472)
pyautogui.write("teste@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.click(x=958, y=667)
time.sleep(2)

#importar base de dados
tabela = pd.read_csv("produtos.csv")

#cadastrar produtos

for linha in tabela.index:
    #codigo do produto
    pyautogui.click(x=701, y=325)
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    #marca do produto
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    #tipo do produto
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    #categoria do produto
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    #preço unitario do produto
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #custo do produto
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #observacoes
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    #enviar
    pyautogui.press("enter")
    pyautogui.scroll(7000)

