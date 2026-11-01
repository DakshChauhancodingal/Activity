import tkinter as tk

root = tk.Tk()
root.title("Multiply Numbers")

tk.Label(root, text="Enter the first number:").pack()
number1 = tk.Entry(root)
number1.pack()

tk.Label(root, text="Enter the second number:").pack()
number2 = tk.Entry(root)
number2.pack()

result = tk.Label(root, text="Product will show here")
result.pack()


def calculate():
    first_number = float(number1.get())
    second_number = float(number2.get())
    answer = first_number * second_number
    result.config(text="Product: " + str(answer))


button = tk.Button(root, text="Multiply", command=calculate)
button.pack()

root.mainloop()