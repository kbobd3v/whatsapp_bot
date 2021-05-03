import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)

position1 = pt.locateOnScreen("./smiley_paperclip.png", confidence=.6)
x = position1[0]
y = position1[1]

# Gets message
def get_message():
    global x, y
    position = pt.locateOnScreen("./smiley_paperclip.png", confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x + 85, y - 56, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(16, -107)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print(f"Message received: {whatsapp_message}")

    return whatsapp_message

# Posts
def post_response(message):
    global x, y
    position = pt.locateOnScreen("./smiley_paperclip.png", confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x + 200, y + 10, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)
    pt.typewrite('\n', interval=.01)

# Processes response

def processes_response(message):
    random_no = random.randrange(3)
    if '?' in str(message).lower():
        return 'No me hagas preguntas'
    else:
        if random_no == 0:
            return 'El bot funciona: Mensaje de prueba 1!'
        elif random_no == 1:
            return 'Seguiremos probando: Mensaje de prueba 2'
        else:
            return 'Tengo hambre: Mensaje de prueba 3'

# Check for new messages

def check_for_new_messages():
    pt.moveTo(x + 84, y - 38, duration=.5)

    while True:
        #Continuously checks for green dots and new messages
        try:
            position = pt.locateOnScreen("./green_circle.png", confidence=.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(.5)

        except(Exception):
            print('No hay usuarios con nuevos mensajes')

        if pt.pixelMatchesColor(int(x + 84), int(y - 38), (255, 255, 255), tolerance=10):
            print('Es blanco')
            processed_message = processes_response(get_message())
            post_response(processed_message)
        else:
            print('No hay nuevos mensajes aun...')
        sleep(5)


check_for_new_messages()