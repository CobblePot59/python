from pynput import mouse, keyboard
import pyscreenshot
from os import path
from datetime import datetime
from termcolor import colored

def screenCap():
    image = pyscreenshot.grab()

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    imageName = f'{timestamp}.png'
    
    imagePath = path.join('screenshot', imageName)
    image.save(imagePath)

def on_click(x, y, button, pressed):
    screenCap()

def on_key_press(key):
    if key == keyboard.Key.esc:
        listener.stop()
        keyboard_listener.stop()

listener = mouse.Listener(on_click=on_click)
listener.start()

keyboard_listener = keyboard.Listener(on_press=on_key_press)
keyboard_listener.start()

print(colored('/!\\ This app take screenshot only in the main screen','red'))
print(colored('\n To stop process press escape','red'))
listener.join()
keyboard_listener.join()