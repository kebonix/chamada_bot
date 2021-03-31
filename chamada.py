import pyautogui
import time
pyautogui.click(x=167, y=751)#abre o chrome
pyautogui.click(x=192, y=52)#clica na barra de pesquisa
pyautogui.typewrite("https://meet.google.com/yyc-cmae-uno")#digita o link(case-sensitive)
pyautogui.typewrite(["enter"])
#dar um jeito de atrasar os hotkeys pra esperar carregar a pagina
time.sleep(6)#TESTANDO TEMPO
pyautogui.hotkey("ctrl", "d")#desabilita camera
pyautogui.hotkey("ctrl", "e")#desabilita mic
time.sleep(3)
pyautogui.click(x=974, y=431)#pede pra participar
time.sleep(3)
pyautogui.moveTo(x=1155, y=92)
pyautogui.click()
#abre o chat
#tem que esperar abrir? EDIT: SIM
time.sleep(3)
pyautogui.click(x=1059, y=616)#clica pra digitar
pyautogui.typewrite("Kawan Braz - 601")#digita nome e mat(case-sensitive)
pyautogui.typewrite(["enter"])#envia mensagem

#todos os intervalos definidos: atentar para os valores case-sensitive
#case-sensitive deve ser substituido por variavel que serve de placeholder pra um input
