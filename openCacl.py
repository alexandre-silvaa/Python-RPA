#script que abre a calculadora do computador

import pyautogui as posicaoMouse

#posicaoMouse.sleep(2) #esse trecho serve para recuperar a posição do mouse e poder definir no código
#print(posicaoMouse.position()) #print na tela a posição do mouse após os segundos definidos acima

#Point(x=18, y=1061) - um monitor 
#Point(x=1297, y=1057) - dois monitores

posicaoMouse.moveTo(x=1297, y=1061) #move o mouse até o posição do menu iniciar
posicaoMouse.click(x=1297, y=1061)  #clica no menu inciar

posicaoMouse.typewrite('calculadora') #procura por calculadora no menu iniciar


#Point(x=406, y=536) - um monitor
#Point(x=1679, y=538) - dois monitores

posicaoMouse.moveTo(x=1679, y=538) #move o mouse até o app calculadora
posicaoMouse.click(x=1679, y=538) #clica em calculadora
