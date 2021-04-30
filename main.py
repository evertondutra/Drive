import pyautogui
import time

pyautogui.alert('O código irá rodar nesse computador, não mova em nada')   # Exibe um alerta no ínicio do código
pyautogui.PAUSE = 1    # A cada linha é esperado 1 segundo para o próximo comando.
# 1 -> abrir o google drive no computador
pyautogui.press('winleft')
pyautogui.write("chrome")
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')

# 2 -> Entrar na minha area de trabalho
pyautogui.hotkey('winleft', 'd')   # pressiona mais de uma tecla ao mesmo tempo
# print(pyautogui.position())  -> mostra a localização que esta o seu mouse no momento
# 3 -> clicar no arquivo que eu quero fazer backup e arrastar ele
pyautogui.moveTo(38, 734)   # move o arquivo
pyautogui.mouseDown()   # Pressiona o botão do mouse
pyautogui.moveTo(675, 662)

# 4 -> Enquanto eu to arrastando, eu vou mudar para o google drive
pyautogui.hotkey('alt', 'tab')

# 5 -> Larguei o arquivo no google drive
pyautogui.mouseUp()

# 6 -> espere 5
time.sleep(10)

pyautogui.alert('O código efetuado com sucessoi')


