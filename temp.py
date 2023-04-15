import random
import time
import sys
import tkinter as tk
from tkinter import *
import threading

root=tk.Tk()

def run_main():
    t = threading.Thread(target=main)
    t.start()

def main():
    type_temp = input('Celsius or Farenheit ')
    temp_promtp = print('What is the temperature? ')
    temp = int(input())
    if type_temp == 'Celsius' or type_temp == 'C' or type_temp == 'c' or type_temp == 'celsius':
        temp_to_f_first = temp * 9/5
        temp_farenheit = temp_to_f_first + 32
        print(temp_farenheit)
    if type_temp == 'Fahrenheit' or type_temp == 'f' or type_temp == 'fahrenheit' or type_temp == 'F':
        temp_to_c_first = temp - 32
        temp_celsius = temp_to_c_first * 5/9
        print(temp_celsius)

#size = Canvas(root, width=500, height=500)
#size.pack()
button = tk.Button(root, text="Temperature Converter", bg="blue", fg="white", command=run_main)
button_end = tk.Button(root, text="Close", bg="red", fg="white", font="bold", width=5, height=1, command=root.destroy)
button.pack()
button_end.pack()

root.mainloop()
