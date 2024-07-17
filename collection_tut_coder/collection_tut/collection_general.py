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
    speak("Opening Notepad.")
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite('notepad', interval=0.25)  # Typing effect with interval
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)

    # Introduction to collections
    speak("Today, we will learn about collections in Java.")
    speak("A collection is a framework that provides an architecture to store and manage a group of objects.")
    speak("The Collections Framework mainly includes four interfaces: List, Set, Queue, and Map.")

    # Explaining List
    speak("The List interface stores elements in an ordered sequence and allows duplicate elements.")
    speak("Some common implementations of the List interface are ArrayList, LinkedList, and Vector.")
    type_text('import java.util.ArrayList;\n', pause=0.1)
    type_text('import java.util.LinkedList;\n', pause=0.1)
    type_text('import java.util.Vector;\n', pause=0.1)
    time.sleep(1)

    # Explaining Set
    speak("The Set interface stores unique elements and does not maintain any order.")
    speak("Some common implementations of the Set interface are HashSet, LinkedHashSet, and TreeSet.")
    type_text('import java.util.HashSet;\n', pause=0.1)
    type_text('import java.util.LinkedHashSet;\n', pause=0.1)
    type_text('import java.util.TreeSet;\n', pause=0.1)
    time.sleep(1)

    # Explaining Queue
    speak("The Queue interface stores elements in a FIFO, or First In First Out, order.")
    speak("Some common implementations of the Queue interface are LinkedList, PriorityQueue, and ArrayDeque.")
    type_text('import java.util.LinkedList;\n', pause=0.1)
    type_text('import java.util.PriorityQueue;\n', pause=0.1)
    type_text('import java.util.ArrayDeque;\n', pause=0.1)
    time.sleep(1)

    # Explaining Map
    speak("The Map interface stores key-value pairs. Each key is unique, and each key maps to exactly one value.")
    speak("Some common implementations of the Map interface are HashMap, LinkedHashMap, and TreeMap.")
    type_text('import java.util.HashMap;\n', pause=0.1)
    type_text('import java.util.LinkedHashMap;\n', pause=0.1)
    type_text('import java.util.TreeMap;\n', pause=0.1)
    time.sleep(1)

    # Explaining and typing a sample code for ArrayList
    speak("Now, let's create a sample program using ArrayList.")
    speak("We will define a class named CollectionExample.")
    type_text('public class CollectionExample {\n', pause=0.1)
    time.sleep(1)

    speak("Inside the main method, we will create an instance of ArrayList to store a list of strings.")
    type_text('    public static void main(String[] args) {\n', pause=0.1)
    type_text('        ArrayList<String> list = new ArrayList<>();\n', pause=0.1)
    time.sleep(1)

    speak("We will add elements to the ArrayList using the add method.")
    type_text('        list.add("Apple");\n', pause=0.1)
    type_text('        list.add("Banana");\n', pause=0.1)
    type_text('        list.add("Cherry");\n', pause=0.1)
    time.sleep(1)

    speak("We will iterate over the elements of the ArrayList using an iterator and print each element.")
    type_text('        for (String fruit : list) {\n', pause=0.1)
    type_text('            System.out.println(fruit);\n', pause=0.1)
    type_text('        }\n', pause=0.1)
    time.sleep(1)

    speak("We will remove an element from the ArrayList using the remove method.")
    type_text('        list.remove("Banana");\n', pause=0.1)
    time.sleep(1)

    speak("Finally, we will print the updated ArrayList.")
    type_text('        System.out.println("Updated list: " + list);\n', pause=0.1)
    type_text('    }\n', pause=0.1)
    type_text('}\n', pause=0.1)
    time.sleep(1)

    speak("Now, we will save this file as CollectionExample.java.")
    pyautogui.hotkey('ctrl', 's')
    time.sleep(2)
    file_path = r'C:\Users\Admin\Desktop\Min DR dsa\collection_tut_coder\collection_tutmport \CollectionExample.java'  # Specify the correct path
    speak(f"Typing the file path {file_path}.")
    type_text(file_path, pause=0.1)
    pyautogui.press('enter')
    time.sleep(2)

    speak("Next, we will open the Command Prompt to compile and run our Java program.")
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite('cmd', interval=0.25)  # Typing effect with interval
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)

    speak("We will navigate to the directory where we saved our Java file.")
    type_text(f'cd {os.path.dirname(file_path)}\n', pause=0.1)
    time.sleep(2)

    speak("We will compile our Java program using javac.")
    type_text('javac CollectionExample.java\n', pause=0.1)
    time.sleep(2)

    speak("Finally, we will run the compiled Java program using the java command.")
    type_text('java CollectionExample\n', pause=0.1)
    time.sleep(2)

# Run the tutorial
tutorial()
