from tkinter import *
import math


def click(what):
    print("You clicked" + what)


def main():
    print('Hello World!')

    window = Tk()
    window.title('Calculator')
    window.geometry('400x600')

    icon = PhotoImage(file='icon.png')
    window.iconphoto(True, icon)

    button7 = Button(window, image=icon, width=30, height=30, command=lambda: click("7")).grid(row=0, column=0)
    button8 = Button(window, image=icon, width=30, height=30, command=lambda: click("8")).grid(row=0, column=1)
    button9 = Button(window, image=icon, width=30, height=30, command=lambda: click("9")).grid(row=0, column=2)
    buttonDiv = Button(window, image=icon, width=30, height=30, command=lambda: click("div")).grid(row=0, column=3)
    button4 = Button(window, image=icon, width=30, height=30, command=lambda: click("4")).grid(row=1, column=0)
    button5 = Button(window, image=icon, width=30, height=30, command=lambda: click("5")).grid(row=1, column=1)
    button6 = Button(window, image=icon, width=30, height=30, command=lambda: click("6")).grid(row=1, column=2)
    buttonMul = Button(window, image=icon, width=30, height=30, command=lambda: click("mul")).grid(row=1, column=3)
    button1 = Button(window, image=icon, width=30, height=30, command=lambda: click("1")).grid(row=2, column=0)
    button2 = Button(window, image=icon, width=30, height=30, command=lambda: click("2")).grid(row=2, column=1)
    button3 = Button(window, image=icon, width=30, height=30, command=lambda: click("3")).grid(row=2, column=2)
    buttonSub = Button(window, image=icon, width=30, height=30, command=lambda: click("sub")).grid(row=2, column=3)
    button0 = Button(window, image=icon, width=30, height=30, command=lambda: click("0")).grid(row=3, column=0)
    buttonDot = Button(window, image=icon, width=30, height=30, command=lambda: click("dot")).grid(row=3, column=1)
    buttonAdd = Button(window, image=icon, width=30, height=30, command=lambda: click("add")).grid(row=3, column=2)
    buttonEqu = Button(window, image=icon, width=30, height=30, command=lambda: click("equ")).grid(row=3, column=3)
    
    window.mainloop()

    return 0


if __name__ == '__main__':
    main()
