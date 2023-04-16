import tkinter as tk

root = tk.Tk()

def run_main():
    t = threading.Thread(target=main)
    t.start()

def main():
    type_temp = input('Celsius or Fahrenheit: ')
    temp_prompt = input('What is the temperature? ')
    temp = float(temp_prompt)
    if type_temp.lower() in ['celsius', 'c']:
        temp_to_f_first = temp * 9/5
        temp_fahrenheit = temp_to_f_first + 32
        print(temp_fahrenheit)
    elif type_temp.lower() in ['fahrenheit', 'f']:
        temp_to_c_first = temp - 32
        temp_celsius = temp_to_c_first * 5/9
        print(temp_celsius)

def convert_temp():
    temp = float(entry_temp.get())
    if var.get() == 1:
        temp_to_f_first = temp * 9/5
        temp_fahrenheit = temp_to_f_first + 32
        label_result.config(text=f"{temp}°C = {temp_fahrenheit}°F")
    else:
        temp_to_c_first = temp - 32
        temp_celsius = temp_to_c_first * 5/9
        label_result.config(text=f"{temp}°F = {temp_celsius}°C")

label_temp = tk.Label(root, text="Enter temperature:")
label_temp.pack()

entry_temp = tk.Entry(root)
entry_temp.pack()

var = tk.IntVar()
check_temp = tk.Checkbutton(root, text="Celsius to Fahrenheit", variable=var)
check_temp.pack()

button_convert = tk.Button(root, text="Convert", command=convert_temp)
button_convert.pack()

label_result = tk.Label(root, text="")
label_result.pack()

button_end = tk.Button(root, text="Close", bg="red", fg="white", font="bold", width=5, height=1, command=root.destroy)
button_end.pack()

root.title("Temperature Converter")
root.mainloop()
