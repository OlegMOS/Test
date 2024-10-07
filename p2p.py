# ДЗ_OP_07 Написать программу на языке программирования Python с использованием модуля Techinter,
# которая позволяет пользователю ввести свое имя в окно ввода, а затем выводить на экран
# сообщение «Привет» и имя, которое было введено. То есть «Привет, Нина», «Привет, Максим», «Привет, Егор» и так далее.

import tkinter as tk

root = tk.Tk()
root.title("Приветствую, как вас зовут? Введите имя, нажмите кнопку и вводите следующее имя:")
root.geometry("800x400")

def hello():
    name = entry.get()
    label = tk.Label(root, text=f"Привет, {name}")
    label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Привет", command=hello)
button.pack()

root.mainloop()