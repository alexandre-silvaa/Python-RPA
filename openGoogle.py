#script que abre o navegador e procura o preço do dólar
import pyautogui as posicaoAbrirGoogle

#Tempo de espera
posicaoAbrirGoogle.sleep(2)

#move o mouse
posicaoAbrirGoogle.moveTo(x=20, y=1060) 
#clica com o mouse
posicaoAbrirGoogle.click(x=20, y=1060) 
#pesquisa no menu
posicaoAbrirGoogle.typewrite('chrome') 

#Tempo de espera
posicaoAbrirGoogle.sleep(2)

#move o mouse
posicaoAbrirGoogle.moveTo(x=187, y=382)
#clica com o mouse
posicaoAbrirGoogle.click(x=187, y=382)

#Tempo de espera
posicaoAbrirGoogle.sleep(2)

#Procuramos o site do google
posicaoAbrirGoogle.typewrite('https://www.google.com/')

#Tempo de espera
posicaoAbrirGoogle.sleep(2)

#Aperta a tecla enter
posicaoAbrirGoogle.press('enter')

#Tempo de espera
posicaoAbrirGoogle.sleep(2)

#Procuramos pelo dolar 
posicaoAbrirGoogle.typewrite('Dolar hoje')

#Tempo de espera
posicaoAbrirGoogle.sleep(2)

#Aperta a tecla enter
posicaoAbrirGoogle.press('enter')