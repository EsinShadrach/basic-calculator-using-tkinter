# done defining all the button functions all that remains is to design the buttons or rather resize
from tkinter import *
from math import *

root = Tk()
root.title = ("calculator")

# for entry box creation
e = Entry(root, width=70, borderwidth=0)
e.grid(row=0, column=0, columnspan=4, padx=50, pady=50)


# to give the buttons a function
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


def button_sin():
    first_number = e.get()
    global f_num
    global math
    math = "sin"
    f_num = int(first_number)
    e.delete(0, END)


def button_cos():
    first_number = e.get()
    global f_num
    global math
    math = "cos"
    f_num = int(first_number)
    e.delete(0, END)


def button_tan():
    first_number = e.get()
    global f_num
    global math
    math = "tan"
    f_num = int(first_number)
    e.delete(0, END)


def button_sqrt():
    first_number = e.get()
    global f_num
    global math
    math = "sqrt"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "sin":
        e.insert(0, sin(int(second_number)))
    if math == "cos":
        e.insert(0, cos(int(second_number)))
    if math == "tan":
        e.insert(0, tan(int(second_number)))
    if math == "sqrt":
        e.insert(0, int(second_number) ** 0.5)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))


# creation of buttons
button_1 = Button(root, text="1", padx=57, pady=20, bg="#FCFCFC", fg="#000000", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=58, pady=20, bg="#FCFCFC", fg="#000000", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=59, pady=20, bg="#FCFCFC", fg="#000000", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=57, pady=20, bg="#FCFCFC", fg="#000000", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=58, pady=20, bg="#FCFCFC", fg="#000000", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=59, pady=20, bg="#FCFCFC", fg="#000000", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=57, pady=20, bg="#FCFCFC", fg="#000000", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=58, pady=20, bg="#FCFCFC", fg="#000000", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=59, pady=20, bg="#FCFCFC", fg="#000000", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=58, pady=20, bg="#FCFCFC", fg="#000000", command=lambda: button_click(0))
button_add = Button(root, text="+", padx=57, pady=20, bg="#7391FF", fg="#000000", command=button_add)
button_equal = Button(root, text="=", padx=58, pady=20, bg="#4EF591", fg="#000000", command=button_equal)
button_clear = Button(root, text="C", fg="#FF1212", bg="#FFF64D", padx=57, pady=20, command=button_clear)
button_subtract = Button(root, text="-", padx=59, pady=20, bg="#7391FF", fg="#000000", command=button_subtract)
button_multiply = Button(root, text="×", padx=57, pady=20, bg="#7391FF", fg="#000000", command=button_multiply)
button_divide = Button(root, text="÷", padx=58, pady=20, bg="#7391FF", fg="#000000", command=button_divide)
button_sin = Button(root, text="sin", padx=54, pady=20, bg="#FF0004", fg="#000000", command=button_sin)
button_cos = Button(root, text="cos", padx=53, pady=20, bg="#FF0004", fg="#000000", command=button_cos)
button_tan = Button(root, text="tan", padx=53, pady=20, bg="#FF0004", fg="#000000", command=button_tan)
button_sqrt = Button(root, text="√", padx=57, pady=20, bg="#7391FF", fg="#000000", command=button_sqrt)

# button packing 1-3
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

# button packing 4-6
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

# button packing 7-9
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

# button packing for 0, CE, and plus
button_clear.grid(row=5, column=0)
button_0.grid(row=4, column=1)
button_add.grid(row=1, column=3)
button_equal.grid(row=5, column=3)

# button packing for multiply, subtract, and divide
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

# sin cos tan and squareroot
button_sin.grid(row=4, column=2)
button_cos.grid(row=5, column=2)
button_tan.grid(row=5, column=1)
button_sqrt.grid(row=4, column=0)

root.mainloop()
