import tkinter as tk
from tkinter import messagebox

def convert_base():
    user_input = choice_var.get()
    
    if user_input == 1:
        number = entry_var.get()
        try:
            result = int(number, 2)
            messagebox.showinfo("ผลลัพธ์", f'แปลงเลขฐาน 2: {number} เป็นฐาน 10: {result}')
        except ValueError:
            messagebox.showerror("ข้อผิดพลาด", "โปรดกรอกตัวเลขที่ถูกต้อง")

    elif user_input == 2:
        number = entry_var.get()
        try:
            hex_number = hex(int(number, 2))[2:].upper()
            messagebox.showinfo("ผลลัพธ์", f'แปลงเลขฐาน 2: {number} เป็นฐาน 16: {hex_number}')
        except ValueError:
            messagebox.showerror("ข้อผิดพลาด", "โปรดกรอกตัวเลขที่ถูกต้อง")

    elif user_input == 3:
        number = entry_var.get()
        try:
            binary_number = bin(int(number, 10))[2:]
            messagebox.showinfo("ผลลัพธ์", f'แปลงเลขฐาน 10: {number} เป็นฐาน 2: {binary_number}')
        except ValueError:
            messagebox.showerror("ข้อผิดพลาด", "โปรดกรอกตัวเลขที่ถูกต้อง")

    elif user_input == 4:
        number = entry_var.get()
        try:
            hex_number = hex(int(number, 10))[2:].upper()
            messagebox.showinfo("ผลลัพธ์", f'แปลงเลขฐาน 10: {number} เป็นฐาน 16: {hex_number}')
        except ValueError:
            messagebox.showerror("ข้อผิดพลาด", "โปรดกรอกตัวเลขที่ถูกต้อง")

    elif user_input == 5:
        number = entry_var.get()
        try:
            binary_number = bin(int(number, 16))[2:]
            messagebox.showinfo("ผลลัพธ์", f'แปลงเลขฐาน 16: {number} เป็นฐาน 2: {binary_number}')
        except ValueError:
            messagebox.showerror("ข้อผิดพลาด", "โปรดกรอกตัวเลขที่ถูกต้อง")

    elif user_input == 6:
        number = entry_var.get()
        try:
            decimal_number = int(number, 16)
            messagebox.showinfo("ผลลัพธ์", f'แปลงเลขฐาน 16: {number} เป็นฐาน 10: {decimal_number}')
        except ValueError:
            messagebox.showerror("ข้อผิดพลาด", "โปรดกรอกตัวเลขที่ถูกต้อง")

root = tk.Tk()
root.title("โปรแกรมแปลงเลขฐาน")
choice_var = tk.IntVar()

choices = [
    ("แปลงเลขฐาน 2 -> 10", 1),
    ("แปลงเลขฐาน 2 -> 16", 2),
    ("แปลงเลขฐาน 10 -> 2", 3),
    ("แปลงเลขฐาน 10 -> 16", 4),
    ("แปลงเลขฐาน 16 -> 2", 5),
    ("แปลงเลขฐาน 16 -> 10", 6),
]

for text, value in choices:
    tk.Radiobutton(root, text=text, variable=choice_var, value=value).pack()

entry_var = tk.Entry(root)
entry_var.pack()
convert_button = tk.Button(root, text="แปลง", command=convert_base)
convert_button.pack()

root.mainloop()
