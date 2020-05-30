#Author @ram
#automatically manipulate mouse movements

import pyautogui 
import time

#To check resolution of screen
#print(pyautogui.size())

#To move to specific location	 
#pyautogui.moveTo(1635, 231, duration = 1)

#To find current location of mouse
#print(pyautogui.position()) 

#To click specific location

while True:
	pyautogui.click(1635, 240)
	time.sleep(60)
