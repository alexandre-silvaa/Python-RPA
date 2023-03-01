#script que abre a calculadora do computador
import pyautogui as posicaoMouse

#Tempo de espera
posicaoMouse.sleep(2)
#print(posicaoMouse.position()) #print na tela a posição do mouse após os segundos definidos acima

#move o mouse
#posicaoMouse.moveTo(x=18, y=1061) #um monitor
#clica no menu inciar
#posicaoMouse.click(x=18, y=1061) 

#move o mouse
posicaoMouse.moveTo(x=1297, y=1061) #dois monitores
#clica no menu inciar
posicaoMouse.click(x=1297, y=1061) 

#procura por calculadora no menu iniciar
posicaoMouse.typewrite('calculadora') 

#move o mouse até o app calculadora
#posicaoMouse.moveTo(x=406, y=572) #um monitor
#clica em calculadora
#posicaoMouse.click(x=406, y=572)

#move o mouse até o app calculadora
posicaoMouse.moveTo(x=1679, y=572) #dois monitores
#clica em calculadora
posicaoMouse.click(x=1679, y=572)
