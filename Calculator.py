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
root.title("Simple Calculator")
root.configure(bg="#222222")
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 14), padding=10)
style.configure("TText", font=("Helvetica", 18), padding=10)
style.map("TButton", foreground=[('pressed', '#ffffff'), ('active', '#333333')],
          background=[('pressed', '!disabled', '#444444'), ('active', '#555555')])

text_result = tk.Text(root, height=2, width=16, font=("Helvetica", 24), bg="#333333", fg="#ffffff", bd=0, padx=10, pady=10)
text_result.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")

buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('x', 3, 3),
    ('(', 4, 0), ('0', 4, 1), (')', 4, 2), ('÷', 4, 3),
    ('C', 5, 0, 2), ('=', 5, 2, 2)
]

for (text, row, col, *cs) in buttons:
    action = lambda x=text: add_to_calculator(x) if x not in {'C', '='} else (clear_field() if x == 'C' else evaluation_calculation())
    ttk.Button(root, text=text, command=action, style="TButton").grid(row=row, column=col, columnspan=cs[0] if cs else 1, padx=5, pady=5, sticky="nsew")
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
root.update_idletasks()
root.minsize(root.winfo_width(), root.winfo_height())
root.geometry(f"{root.winfo_width()}x{root.winfo_height()}")

root.mainloop()
