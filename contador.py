import pyautogui as auto
import time

auto.keyDown('win')
auto.press('r')
auto.keyUp('win')
auto.write("notepad")
auto.press('enter')
auto.PAUSE=2

count = 1
while count < 100:
    count += 1
    escreva = count

    auto.write('escreva')

