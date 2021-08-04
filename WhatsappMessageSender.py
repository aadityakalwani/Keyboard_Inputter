import pyautogui
import time

# these are commands i can do, try to learn these as well

# >>> screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen.
# (The primary monitor, in multi-monitor setups.)
# >>> currentMouseX, currentMouseY = pyautogui.position()
# Returns two integers, the x and y of the mouse cursor's current position.

# >>> pyautogui.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
# >>> pyautogui.click() # Click the mouse at its current location.
# >>> pyautogui.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
# >>> pyautogui.move(None, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
# >>> pyautogui.doubleClick() # Double click the mouse

# >>> pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
# Use tweening/easing function to move mouse over 2 seconds.

# >>> pyautogui.write('Hello world!', interval=0.25)
# Type with quarter-second pause in between each key.

# >>> pyautogui.press('esc') # Simulate pressing the Escape key.
# >>> pyautogui.keyDown('shift')
# >>> pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
# >>> pyautogui.keyUp('shift')
# >>> pyautogui.hotkey('ctrl', 'c')

# this is where i'd put my instructions:

name = input("Enter the name of the person you would like to send a message to: ")
message = input("Enter what you want the message to say: ")
amount_of_times = int(input("Enter how many times you want this message to send: "))
wait_time = float(input("Enter how long you want the gap to be between messages: "))
time_interval = float(input("Enter the amount of time you would like there to be between each character typed: "))
message_counter = input("Enter y if you want there to be a message counter, and n for no message counter: ")


def open_whatsapp():
    pyautogui.keyDown("command")
    pyautogui.press("space")
    pyautogui.keyUp("command")
    pyautogui.write("whatsapp", interval=0.25)
    pyautogui.press("enter")
    # whatsapp is now opened


def custom_chat_open():
    pyautogui.keyDown("command")
    pyautogui.press("f")
    pyautogui.keyUp("command")
    pyautogui.write(name, interval=0.25)
    pyautogui.press("enter")


def write_message():
    if message_counter.lower() == "n":
        pyautogui.write(message, interval=time_interval)
    elif message_counter.lower() == "y":
        pyautogui.write(f"{message} ({i+1}/{amount_of_times})", interval=time_interval)
    pyautogui.press("enter")
    # message has been sent


open_whatsapp()
time.sleep(3)
custom_chat_open()
time.sleep(3)

i = 0
while i < amount_of_times:
    write_message()
    i += 1
    time.sleep(wait_time)
