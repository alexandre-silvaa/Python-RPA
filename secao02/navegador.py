#trabalhar com páginas da web
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import para tempo de pausa 
import pyautogui as tempo
#import para usar teclas
import pyautogui as tecla
#By serve para trabalhar com as atualizações mais recentes
from selenium.webdriver.common.by import By
import xlsxwriter
import os

#autprização para acessar configurações do chrome
navegador = webdriver.Chrome()
navegador.get("https://www.google.com.br/")
tempo.sleep(2)

#---------------------------------------------- DOLAR -------------------------------------------------------#

#Digita na caixa de pesquisa
navegador.find_element(By.NAME, 'q').send_keys('Dolar hoje')
tempo.sleep(2)

#Tecla enter
navegador.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
tempo.sleep(2)

#recebe o XPATH do item na tela e pegamos o primeiro valor da lista
dolar = navegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
print(dolar)

#---------------------------------------------- EURO -------------------------------------------------------#
tempo.sleep(2)

#retorna para a caixa de pesquisa
navegador.find_element(By.NAME, 'q').send_keys("")
tempo.sleep(2)

#apertar tab
tecla.press('tab')
tempo.sleep(2)
#apertar enter para limpar campo de pesquisa
tecla.press('enter')

#Digita na caixa de pesquisa
navegador.find_element(By.NAME, 'q').send_keys('Euro hoje')
tempo.sleep(2)

#Tecla enter
navegador.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
tempo.sleep(2)

#recebe o XPATH do item na tela e pegamos o primeiro valor da lista
euro = navegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
print(euro)

#---------------------------------------------- EXCEL -------------------------------------------------------#

url = "C:\workspace\Python-RPA\secao02\Dolar e Euro.xlsx"
planilha = xlsxwriter.Workbook(url)
cotacao = planilha.add_worksheet()

dolar = dolar.replace(',','.')
euro = euro.replace(',','.')

dolar = float(dolar)
euro = float(euro)

#escreve nas células
cotacao.write("A1","Dolar")
cotacao.write("B1","Euro")
cotacao.write("A2",dolar)
cotacao.write("B2",euro)

planilha.close()

os.startfile(url)


