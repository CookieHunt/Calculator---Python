from tkinter import *
import math


def click(what):
    print("You clicked" + what)


class Calculator:
    def __init__(self):
        self.variable = 0.0
        self.operation = 'num'
        self.secondvariable = 0.0
        self.float = 0
        self.variablestring = ''
        self.variabletoshow = StringVar()
        self.variabletoshow.set("0")

    def display(self):
        self.variabletoshow.set(self.variablestring)

    def addnumber(self, number):
        if self.operation == 'num':
            if self.float == 0:
                self.variable = self.variable * 10 + number
                print(self.variable)
                self.variablestring += str(number)
                #print(self.variablestring)
                self.display()
            else:
                self.variable = self.variable + number / self.float
                print(self.variable)
                self.variablestring += str(number)
                self.float *= 10
                self.display()
        else:
            if self.float == 0:
                self.secondvariable = self.secondvariable * 10 + number
                print(self.secondvariable)
                self.variablestring += str(number)
                #print(self.variablestring)
                self.display()
            else:
                self.secondvariable = self.secondvariable + number / self.float
                print(self.secondvariable)
                self.variablestring += str(number)
                self.float *= 10
                self.display()


    def isfloat(self):
        if self.float == 0:
            self.float = 10
            self.variablestring += str('.')
            self.display()

    def simpleaction(self, action):
        self.operation = action
        self.variablestring = ''
        self.variabletoshow.set('0')
        self.float = 0








def main():
    print('Hello World!')



    window = Tk()
    window.title('Calculator')
    window.geometry('400x600')
    window.iconphoto(True, PhotoImage(file='icon.png'))

    calculator = Calculator()

    image = PhotoImage(file='icon.png')

    label = Label(window, textvariable=calculator.variabletoshow)
    label.pack()

    frame = Frame(window)
    frame.pack()

    button7 = Button(frame, image=image, width=30, height=30, command=lambda: calculator.addnumber(7))
    button7.grid(row=0, column=0)
    button8 = Button(frame, image=image, width=30, height=30, command=lambda: calculator.addnumber(8))
    button8.grid(row=0, column=1)
    button9 = Button(frame, image=image, width=30, height=30, command=lambda: calculator.addnumber(9))
    button9.grid(row=0, column=2)
    buttonDiv = Button(frame, image=image, width=30, height=30, command=lambda: click("7"))
    buttonDiv.grid(row=0, column=3)
    button4 = Button(frame, image=image, width=30, height=30, command=lambda: calculator.addnumber(4))
    button4.grid(row=1, column=0)
    button5 = Button(frame, image=image, width=30, height=30, command=lambda: calculator.addnumber(5))
    button5.grid(row=1, column=1)
    button6 = Button(frame, image=image, width=30, height=30, command=lambda: calculator.addnumber(6))
    button6.grid(row=1, column=2)
    buttonMul = Button(frame, image=image, width=30, height=30, command=lambda: click("7"))
    buttonMul.grid(row=1, column=3)
    button1 = Button(frame, image=image, width=30, height=30, command=lambda: calculator.addnumber(1))
    button1.grid(row=2, column=0)
    button2 = Button(frame, image=image, width=30, height=30, command=lambda: calculator.addnumber(2))
    button2.grid(row=2, column=1)
    button3 = Button(frame, image=image, width=30, height=30, command=lambda: calculator.addnumber(3))
    button3.grid(row=2, column=2)
    buttonSub = Button(frame, image=image, width=30, height=30, command=lambda: click("7"))
    buttonSub.grid(row=2, column=3)
    button0 = Button(frame, image=image, width=30, height=30, command=lambda: calculator.addnumber(0))
    button0.grid(row=3, column=0)
    buttonDot = Button(frame, image=image, width=30, height=30, command=lambda: calculator.isfloat())
    buttonDot.grid(row=3, column=1)
    buttonAdd = Button(frame, image=image, width=30, height=30, command=lambda: calculator.simpleaction('add'))
    buttonAdd.grid(row=3, column=2)
    buttonEqu = Button(frame, image=image, width=30, height=30, command=lambda: click("7"))
    buttonEqu.grid(row=3, column=3)

    window.mainloop()


if __name__ == '__main__':
    main()
