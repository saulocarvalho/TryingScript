import pyautogui

pyautogui.keyDown('alt')
pyautogui.press(['tab']) #Nesse caso pode ser passado mais de um valor
pyautogui.keyUp('alt')

pyautogui.write("Ola Mundo!")