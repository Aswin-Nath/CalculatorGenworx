import tkinter as tk
from add import add
from sub import sub
from mul import mul
from div import div
from mul import mul

def perform_calc(operation):
    try:
        val1 = float(input1.get())
        val2 = float(input2.get())

        if operation == "add":
            output.set(add(val1, val2))
        elif operation == "sub":
            output.set(sub(val1, val2))
        elif operation == "mul":
            output.set(mul(val1, val2))
        elif operation == "div":
            output.set(div(val1, val2))
    except Exception:
        output.set("Invalid Entry")

window = tk.Tk()
window.title("Calculator")
window.geometry("300x300")

tk.Label(window, text="First Number:").pack()
input1 = tk.Entry(window)
input1.pack()

tk.Label(window, text="Second Number:").pack()
input2 = tk.Entry(window)
input2.pack()

output = tk.StringVar()
tk.Label(window, text="Result:", font=("Arial", 11)).pack(pady=4)
tk.Label(window, textvariable=output, font=("Arial", 12), fg="darkblue").pack()

tk.Button(window, text="+ Add", width=12, command=lambda: perform_calc("add")).pack(pady=3)
tk.Button(window, text="- Subtract", width=12, command=lambda: perform_calc("sub")).pack(pady=3)
tk.Button(window, text="x Multiply", width=12, command=lambda: perform_calc("mul")).pack(pady=3)
tk.Button(window, text="/ Divide", width=12, command=lambda: perform_calc("div")).pack(pady=3)

window.mainloop()