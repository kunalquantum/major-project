import pygetwindow as gw
import pyautogui
import time
import os

def open_powerpoint(file_path):
    os.system(f'start powerpnt "{file_path}"')
    time.sleep(5)  # Wait for PowerPoint to open

def open_cmd():
    os.system("start cmd")
    time.sleep(3)  # Wait for cmd to open

def focus_window(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if windows:
        windows[0].activate()
    else:
        print(f"No window found with title: {window_title}")

# Path to the saved PowerPoint file
powerpoint_file_path = r"E:\SAMARTHYA.pptx"  # Adjust the path to your file

# Open PowerPoint with the specific file and Command Prompt
open_powerpoint(powerpoint_file_path)
pyautogui.hotkey('f5')
for i in range(10):
    time.sleep(2)
    pyautogui.hotkey('End')
open_cmd()

# Switch between PowerPoint and Command Prompt a few times
for _ in range(3):
    focus_window("SAMARTHYA - PowerPoint")  # Adjust this title if needed
    time.sleep(2)  # Wait for 2 seconds in PowerPoint
    pyautogui.hotkey('alt','tab')  # Adjust this title if needed
    time.sleep(2)  # Wait for 2 seconds in cmd
