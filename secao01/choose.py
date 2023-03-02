#script que abre um menu de escolhas de aplicativos
import pyautogui
import pyautogui as escolha_opcao

opcao = pyautogui.confirm('Escolha uma opção', buttons = ['Excel','Word','Notepad'])

if opcao == 'Excel':

    escolha_opcao.hotkey('win','r')     #pressiona duas teclas ao mesmo tempo
    escolha_opcao.sleep(2)              #tempo de espera
    escolha_opcao.typewrite('Excel')    #digita excel
    escolha_opcao.press('enter')        #pressiona enter
    escolha_opcao.sleep(2)              #tempo de espera
    escolha_opcao.click(x=343, y=275)   #clica em uma nova planilha
    escolha_opcao.typewrite('Escolhi abrir o Excel')    
    
elif opcao == 'Word':
    
    escolha_opcao.hotkey('win','r')     #pressiona duas teclas ao mesmo tempo
    escolha_opcao.sleep(2)              #tempo de espera
    escolha_opcao.typewrite('winword')  #digita winwrod
    escolha_opcao.press('enter')        #pressiona enter
    escolha_opcao.sleep(2)              #tempo de espera
    escolha_opcao.click(x=343, y=275)   #clica em uma nova planilha
    escolha_opcao.typewrite('Escolhi abrir o Word')

elif opcao == 'Notepad':

    escolha_opcao.hotkey('win','r')     #pressiona duas teclas ao mesmo tempo
    escolha_opcao.sleep(2)              #tempo de espera
    escolha_opcao.typewrite('notepad')  #digita notepad
    escolha_opcao.press('enter')        #pressiona enter
    escolha_opcao.sleep(2)              #tempo de espera
    escolha_opcao.typewrite('Escolhi abrir o Notepad')