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
    # Open Notepad
    speak("Opening Notepad to write a simple example of Queue usage.")
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite('Notepad', interval=0.25)  
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)  # Adjust time based on your system speed

    # Introduction to Queue
    speak("Let's understand the Queue interface in Java with a practical example.")
    speak("A Queue represents a collection of elements with the First In First Out (FIFO) principle.")
    speak("For this example, imagine a help desk ticketing system.")

    # Explain the scenario
    speak("In a help desk system, customers submit tickets for assistance.")
    speak("Tickets are processed in the order they are received, just like a queue.")

    # Write Java code to implement Queue
    type_text('// Java code to implement a help desk ticketing system using Queue\n')
    type_text('import java.util.LinkedList;\n')
    type_text('import java.util.Queue;\n\n')
    type_text('public class HelpDesk {\n')
    type_text('    public static void main(String[] args) {\n')
    type_text('        Queue<String> tickets = new LinkedList<>();\n')
    type_text('        tickets.add("Ticket 1: Network issue");\n')
    type_text('        tickets.add("Ticket 2: Software problem");\n')
    type_text('        tickets.add("Ticket 3: Printer malfunction");\n\n')
    type_text('        // Processing tickets\n')
    type_text('        while (!tickets.isEmpty()) {\n')
    type_text('            String ticket = tickets.poll();\n')
    type_text('            System.out.println("Processing: " + ticket);\n')
    type_text('            // Code to handle the ticket...\n')
    type_text('        }\n')
    type_text('        System.out.println("All tickets processed.");\n')
    type_text('    }\n')
    type_text('}\n')

    # Save the file
    speak("Now, let's save this code as HelpDesk.java.")
    pyautogui.hotkey('ctrl', 's')
    time.sleep(2)
    file_path = r'C:\path\to\your\directory\HelpDesk.java'  # Specify the correct path
    speak(f"Typing the file path {file_path}.")
    type_text(file_path, pause=0.1)
    pyautogui.press('enter')
    time.sleep(2)

    # Open Command Prompt
    speak("Next, let's open Command Prompt to compile and run our Java program.")
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite('cmd', interval=0.25)  
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)

    # Navigate to the directory
    speak("We will navigate to the directory where we saved our Java file.")
    type_text(f'cd {os.path.dirname(file_path)}\n', pause=0.1)
    time.sleep(2)

    # Compile the Java program
    speak("We will compile our Java program using javac.")
    type_text('javac HelpDesk.java\n', pause=0.1)
    time.sleep(2)

    # Run the compiled Java program
    speak("Finally, we will run the compiled Java program.")
    type_text('java HelpDesk\n', pause=0.1)
    time.sleep(2)

# Run the tutorial
tutorial()
