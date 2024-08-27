import tkinter as tk
from tkinter import ttk
calculation = ""

def add_to_calculator(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluation_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")
    
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
   
   
root = tk.Tk()
root.geometry("340x400")

text_result = tk.Text(root, height=2, width=16, font=("Helvetica", 24), bg="#333333", fg="#ffffff", bd=0)
text_result.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculator(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1,sticky="nsew")
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculator(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2,sticky="nsew")
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculator(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3,sticky="nsew")
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculator(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1,sticky="nsew")
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculator(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2,sticky="nsew")
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculator(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3,sticky="nsew")
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculator(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1,sticky="nsew")
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculator(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2,  sticky="nsew")
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculator(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3,sticky="nsew")
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculator(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2, sticky="nsew")
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculator("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4,sticky="nsew")
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculator("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4, sticky="nsew")
btn_mul = tk.Button(root, text="x", command=lambda: add_to_calculator("*"), width=5, font=("Arial", 14))
btn_mul.grid(row=4, column=4,sticky="nsew")
btn_div = tk.Button(root, text="÷", command=lambda: add_to_calculator("/"), width=5, font=("Arial", 14))
btn_div.grid(row=5, column=4,sticky="nsew")
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculator("("), width=5, font=("Arial", 14))
btn_open.grid(row=5, column=1,sticky="nsew")
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculator(")"), width=5, font=("Arial", 14))
btn_close.grid(row=5, column=3,sticky="nsew")
btn_clear = tk.Button(root, text="clear", command=clear_field, width=11, font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2, sticky="nsew")
btn_equals = tk.Button(root, text="=", command=evaluation_calculation, width=11, font=("Arial", 14))
btn_equals.grid(row=6, column=3, columnspan=2, sticky="nsew")

text_result = tk.Text(root, height=2, width=16, font=("Helvetica", 24), bg="green", fg="#ffffff", bd=0)
text_result.grid(row=0, column=0, columnspan=5, pady=10, padx=10,sticky="nsew" )


root.title("Simple Calculator")

root.configure(bg="#222222")
root.grid_rowconfigure(0, weight=1)
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i-1, weight=1)

 

root.mainloop()