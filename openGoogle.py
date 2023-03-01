#script que abre o navegador e procura o preço do dólar
import pyautogui as posicaoAbrirGoogle

#Tempo de espera
posicaoAbrirGoogle.sleep(4)

### um monitor ###
#posicaoAbrirGoogle.moveTo(x=18, y=1061)
#posicaoAbrirGoogle.click(x=18, y=1061) 

### dois monitores ###
posicaoAbrirGoogle.moveTo(x=1297, y=1061) 
posicaoAbrirGoogle.click(x=1297, y=1061) 

#pesquisa no menu
posicaoAbrirGoogle.typewrite('chrome') 

### um monitor ###
#posicaoAbrirGoogle.moveTo(x=406, y=572)
#posicaoAbrirGoogle.click(x=406, y=572)

### dois monitores ###
posicaoAbrirGoogle.moveTo(x=1679, y=572) 
posicaoAbrirGoogle.click(x=1679, y=572)

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