import pyautogui
import time

#pyautogui.click('windows2.png')
#pyautogui.write("notepad")
pyautogui.PAUSE=1
pyautogui.keyDown('win')
pyautogui.press('r')
pyautogui.keyUp('win')
pyautogui.write("notepad")
pyautogui.press('enter')
pyautogui.write("Minha nossa :0 abriu sozinho")
pyautogui.write("\n voce esta sendo hackeado pelo #saulinhohacker")

#pip install auto-py-to-exe // auto-py-to-exe
#interval=1 (1 segundo de pause entre cada tela, ex = n o t e p a d)
