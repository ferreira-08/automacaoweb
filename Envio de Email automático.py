import pyautogui
import time


pyautogui.press('win')
time.sleep(3)

#abrir chrome
pyautogui.write('chrome')
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)

#entrar na conta do chrome
pyautogui.click(583,493)
time.sleep(3)
pyautogui.press('enter')
time.sleep(5)

#Abrir email
pyautogui.click(-277,-220)
time.sleep(6)
pyautogui.click(-2302,-147)
time.sleep(3)
pyautogui.click(-686,196)
time.sleep(5)
pyautogui.write('endereço do Email')
pyautogui.click(-799,248)
time.sleep(5)
pyautogui.write('Assunto')
time.sleep(5)
pyautogui.click(-739,313)
time.sleep(5)
pyautogui.write('Escrever Email')
time.sleep(5)
pyautogui.click(-752,839)

