#script para pegar a posição do mouse na tela
import pyautogui as posicaoMouse

#Tempo de espera
posicaoMouse.sleep(6)
#print na tela a posição do mouse após os segundos definidos acima
print(posicaoMouse.position())
