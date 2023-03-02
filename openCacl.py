#script que abre a calculadora do computador
import pyautogui as posicaoMouse

#move o mouse
posicaoMouse.moveTo(x=20, y=1060) 
#clica no menu inciar
posicaoMouse.click(x=20, y=1060) 

#Tempo de espera
posicaoMouse.sleep(2)

#procura por calculadora no menu iniciar
posicaoMouse.typewrite('calculadora') 

#Tempo de espera
posicaoMouse.sleep(2)

#move o mouse até o app calculadora
posicaoMouse.moveTo(x=187, y=382)
#clica em calculadora
posicaoMouse.click(x=187, y=382)
