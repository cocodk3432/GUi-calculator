# calculator GUI 
import tkinter as tk

root = tk.Tk()

def calculate():
    global result
    result = int(num1.get()) + int(num2.get())
    result_label.config(text=result)
    result_label.grid(row=1, column=1)
    num1.delete(0, tk.END)
    num2.delete(0, tk.END)
    
def clear():
    global result
    result = 0
    result_label.config(text=result)
    result_label.grid(row=1, column=1)
    num1.delete(0, tk.END)
    num2.delete(0, tk.END)
    
def add():
    global result
    result = int(num1.get()) + int(num2.get())
    result_label.config(text=result)
    result_label.grid(row=1, column=1)
    num1.delete(0, tk.END)
    num2.delete(0, tk.END)
    
def subtract():
    global result
    result = int(num1.get()) - int(num2.get())
    result_label.config(text=result)
    result_label.grid(row=1, column=1)
    num1.delete(0, tk.END)
    num2.delete(0, tk.END)
    
def multiply():
    global result
    result = int(num1.get()) * int(num2.get())
    result_label.config(text=result)
    result_label.grid(row=1, column=1)
    num1.delete(0, tk.END)
    num2.delete(0, tk.END)
    
def divide():
    global result
    result = int(num1.get()) / int(num2.get())
    result_label.config(text=result)
    result_label.grid(row=1, column=1)
    num1.delete(0, tk.END)
    num2.delete(0, tk.END)
    
def equal():
    global result
    result = int(num1.get()) + int(num2.get())
    result_label.config(text=result)
    result_label.grid(row=1, column=1)
    num1.delete(0, tk.END)
    num2.delete(0, tk.END)
    
# calculator buttons

num1_label = tk.Label(root, textvariable=tk.StringVar())
num1_label.grid(row=0, column=0)

num2_label = tk.Label(root, textvariable=tk.StringVar())
num2_label.grid(row=0, column=1)

result_label = tk.Label(root, textvariable=tk.StringVar())

num1 = tk.Entry(root)

num2 = tk.Entry(root)

num1.grid(row=0, column=0)

num2.grid(row=0, column=1)

result_label.grid(row=1, column=1)

num1_label.grid(row=0, column=0)

num2_label.grid(row=0, column=1)

add_button = tk.Button(root, text="Add", command=add)

subtract_button = tk.Button(root, text="Subtract", command=subtract)

multiply_button = tk.Button(root, text="Multiply", command=multiply)

divide_button = tk.Button(root, text="Divide", command=divide)

equal_button = tk.Button(root, text="Equal", command=equal)

clear_button = tk.Button(root, text="Clear", command=clear)

add_button.grid(row=1, column=0)

subtract_button.grid(row=1, column=2)

multiply_button.grid(row=1, column=4)

divide_button.grid(row=1, column=6)

equal_button.grid(row=1, column=8)

clear_button.grid(row=1, column=10)

root.mainloop()
