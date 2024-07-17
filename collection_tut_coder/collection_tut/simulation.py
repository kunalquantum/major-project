import pyautogui
import time
import os
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak out text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to type out text with a pause for typing effect
def type_text(text, pause=0.1):
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(pause)

# Explanation and drawing sequence
def tutorial():
    # Open Excel
    speak("Let's use Excel to visualize the FIFO (First In, First Out) queue.")
    speak("We'll simulate enqueue and dequeue operations.")

    speak("Opening Excel...")
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite('Excel', interval=0.25)  
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(8)  # Adjust time based on your system speed

    # Draw a FIFO queue diagram
    speak("Let's draw a FIFO queue diagram.")
    pyautogui.hotkey('alt', 'n')  # Activate insert tab
    time.sleep(0.5)
    pyautogui.typewrite('n')  # Select Shapes
    time.sleep(0.5)
    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])  # Choose arrow shape
    time.sleep(0.5)
    pyautogui.click(x=150, y=150)  # Click to draw first box
    pyautogui.dragTo(x=200, y=50, duration=0.5)  # Draw line to second box
    time.sleep(0.5)
    pyautogui.click(x=200, y=50)  # Click to draw second box
    pyautogui.dragTo(x=200, y=150, duration=0.5)  # Draw line to third box
    time.sleep(0.5)
    pyautogui.click(x=200, y=150)  # Click to draw third box
    pyautogui.dragTo(x=50, y=150, duration=0.5)  # Draw line back to first box
    time.sleep(1)

    # Explain the diagram
    speak("This diagram represents a FIFO queue.")
    speak("Elements are added to the back of the queue (enqueue) and removed from the front (dequeue).")

    # Simulate enqueue and dequeue operations
    speak("Let's simulate enqueue and dequeue operations.")
    pyautogui.click(x=50, y=100)  # Click the first box (front of the queue)
    speak("Enqueuing element 1...")
    pyautogui.typewrite('1', interval=0.1)  # Type 1 to simulate enqueue
    time.sleep(1)

    pyautogui.click(x=50, y=200)  # Click the third box (back of the queue)
    speak("Enqueuing element 2...")
    pyautogui.typewrite('2', interval=0.1)  # Type 2 to simulate enqueue
    time.sleep(1)

    pyautogui.click(x=200, y=100)  # Click the second box (middle of the queue)
    speak("Dequeuing element 1...")
    pyautogui.press('backspace')  # Simulate dequeue by erasing the text
    time.sleep(1)

    pyautogui.click(x=50, y=100)  # Click the first box (front of the queue)
    speak("Dequeuing element 2...")
    pyautogui.press('backspace')  # Simulate dequeue by erasing the text
    time.sleep(1)

    speak("Now, the queue is empty.")

# Run the tutorial
tutorial()
