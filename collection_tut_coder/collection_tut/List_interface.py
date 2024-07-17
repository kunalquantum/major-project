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

# Explanation and typing sequence
def tutorial():
    # Open VS Code
    speak("Opening Notepad")
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite('Notepad', interval=0.25)  
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)  # Adjust time based on your system speed

    # Introduction to lists
    speak("Today, let's learn about lists in Python.")
    speak("A list is a collection which is ordered and changeable. It allows duplicate members.")
    speak("We'll use a problem from LeetCode to illustrate the concept.")

    # Open a browser and navigate to LeetCode
    speak("Let's open a browser and go to LeetCode.")
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    pyautogui.typewrite('https://leetcode.com', interval=0.1)
    pyautogui.press('enter')
    time.sleep(5)  # Adjust time based on your internet speed

    # Choose a problem (e.g., Two Sum)
    speak("For demonstration, we'll use the 'Two Sum' problem.")
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)
    pyautogui.typewrite('Two Sum', interval=0.1)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)

    # Explain the problem
    speak("The 'Two Sum' problem asks to find two numbers such that they add up to a specific target.")
    speak("We are given an array of integers and we need to return the indices of the two numbers.")
    speak("Let's write the solution in Python.")

    # Type out the solution code
    type_text('# Function to find indices of two numbers that add up to target\n')
    type_text('def two_sum(nums, target):\n')
    type_text('    num_dict = {}\n')
    type_text('    for i, num in enumerate(nums):\n')
    type_text('        complement = target - num\n')
    type_text('        if complement in num_dict:\n')
    type_text('            return [num_dict[complement], i]\n')
    type_text('        num_dict[num] = i\n')
    type_text('    return None\n')

    # Save the file
    speak("Now, let's save this code.")
    pyautogui.hotkey('ctrl', 's')
    time.sleep(2)
    file_path = r'\two_sum.py'  # Specify the correct path
    speak(f"Typing the file path {file_path}.")
    type_text(file_path, pause=0.1)
    pyautogui.press('enter')
    time.sleep(2)

    # Run the code
    speak("Let's run this code to see if it works.")
    pyautogui.hotkey('ctrl', 'shift', 'x')
    time.sleep(2)
    pyautogui.typewrite('python two_sum.py', interval=0.1)
    pyautogui.press('enter')
    time.sleep(5)

# Run the tutorial
tutorial()
