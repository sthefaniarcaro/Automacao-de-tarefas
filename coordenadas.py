import time
import pyautogui

time.sleep(5) # leva 5seg para executar as proximas linhas de cod

print(pyautogui.position()) # vai exibir no terminal a posicao do cursor

pyautogui.scroll(1000) # positivo para scroll para cima e negativo para baixo