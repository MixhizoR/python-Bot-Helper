import keyboard
import time
import pyautogui as pag

while True:
    if keyboard.is_pressed('q') == True:
        x,y=pag.position()
        print(f"coords, x={x}, y={y}")
        print(pag.pixel(x,y))
        time.sleep(0.1)
    time.sleep(0.1)