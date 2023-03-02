#script que abre o executar e o editor de texto
import pyautogui as posicaoAbreNotepad

#hotkey permite usar mais de uma tecla para executar comandos
#abre o terminal linux
posicaoAbreNotepad.hotkey('win','r')

#Tempo de espera
posicaoAbreNotepad.sleep(2)

#digite "xed", comando para abrir o editor de texto no terminal
posicaoAbreNotepad.typewrite('notepad')

#Aperta a tecla enter
posicaoAbreNotepad.press('enter')

#Tempo de espera
posicaoAbreNotepad.sleep(2)

#digitamos dentro do editor
posicaoAbreNotepad.typewrite('Abrimos o editor de texto com um robo/script')

#Tempo de espera
posicaoAbreNotepad.sleep(2)

#recupera a janela que está ativa no momento
fecharJanela = posicaoAbreNotepad.getActiveWindow()

#fecha a janela ativa
fecharJanela.close()

#Tempo de espera
posicaoAbreNotepad.sleep(2)

#Aperta a tecla tab
posicaoAbreNotepad.press('tab')

#Tempo de espera
posicaoAbreNotepad.sleep(2)

#Aperta a tecla enter
posicaoAbreNotepad.press('enter')