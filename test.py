from tkinter import *


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
                # print(self.variablestring)
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
                # print(self.variablestring)
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
        if self.operation == 'num':
            self.operation = action
            self.secondvariable = 0.0
            self.variablestring = ''
            self.variabletoshow.set('0')
            self.float = 0


    def equal(self):

        if self.operation == 'add':
            self.variable += self.secondvariable
            self.secondvariable = 0.0
            self.variablestring = str(self.variable)
            self.display()
            self.operation = 'num'

        elif self.operation == 'sub':
            self.variable -= self.secondvariable
            self.secondvariable = 0.0
            self.variablestring = str(self.variable)
            self.display()
            self.operation = 'num'
        elif self.operation == 'mul':

            self.variable *= self.secondvariable
            self.secondvariable = 0.0
            self.variablestring = str(self.variable)
            self.display()
            self.operation = 'num'
        elif self.operation == 'div':
            try:
                self.variable /= self.secondvariable
                self.secondvariable = 0.0
                self.variablestring = str(self.variable)
                self.display()
                self.operation = 'num'
            except ZeroDivisionError:
                self.variable = 0.0
                self.secondvariable = 0.0
                self.variablestring = ''
                self.variabletoshow.set('0')

        elif self.operation == 'num':
            self.variable = 0.0
            self.secondvariable = 0.0
            self.variablestring = ''
            self.variabletoshow.set('0')

        self.float = 0


def main():
    print('Hello World!')

    window = Tk()
    window.title('Calculator')
    window.geometry('430x455')
    window.iconphoto(True, PhotoImage(file='icon.png'))

    calculator = Calculator()

    image1 = PhotoImage(file='1.png')
    image2 = PhotoImage(file='2.png')
    image3 = PhotoImage(file='3.png')
    image4 = PhotoImage(file='4.png')
    image5 = PhotoImage(file='5.png')
    image6 = PhotoImage(file='6.png')
    image7 = PhotoImage(file='7.png')
    image8 = PhotoImage(file='8.png')
    image9 = PhotoImage(file='9.png')
    image0 = PhotoImage(file='0.png')
    imageequ = PhotoImage(file='equ.png')
    imagedot = PhotoImage(file='dot.png')
    imageadd = PhotoImage(file='add.png')
    imagesub = PhotoImage(file='sub.png')
    imagemul = PhotoImage(file='mul.png')
    imagediv = PhotoImage(file='div.png')
    imagebg = PhotoImage(file='numbersbg.png')

    label = Label(window, textvariable=calculator.variabletoshow, font=('Helvetica'))
    label.pack()

    frame = Frame(window)
    frame.pack()


    button7 = Button(frame, image=image7, width=100, height=100, command=lambda: calculator.addnumber(7))
    button7.grid(row=0, column=0)
    button8 = Button(frame, image=image8, width=100, height=100, command=lambda: calculator.addnumber(8))
    button8.grid(row=0, column=1)
    button9 = Button(frame, image=image9, width=100, height=100, command=lambda: calculator.addnumber(9))
    button9.grid(row=0, column=2)
    buttonDiv = Button(frame, image=imagediv, width=100, height=100, command=lambda: calculator.simpleaction('div'))
    buttonDiv.grid(row=0, column=3)
    button4 = Button(frame, image=image4, width=100, height=100, command=lambda: calculator.addnumber(4))
    button4.grid(row=1, column=0)
    button5 = Button(frame, image=image5, width=100, height=100, command=lambda: calculator.addnumber(5))
    button5.grid(row=1, column=1)
    button6 = Button(frame, image=image6, width=100, height=100, command=lambda: calculator.addnumber(6))
    button6.grid(row=1, column=2)
    buttonMul = Button(frame, image=imagemul, width=100, height=100, command=lambda: calculator.simpleaction('mul'))
    buttonMul.grid(row=1, column=3)
    button1 = Button(frame, image=image1, width=100, height=100, command=lambda: calculator.addnumber(1))
    button1.grid(row=2, column=0)
    button2 = Button(frame, image=image2, width=100, height=100, command=lambda: calculator.addnumber(2))
    button2.grid(row=2, column=1)
    button3 = Button(frame, image=image3, width=100, height=100, command=lambda: calculator.addnumber(3))
    button3.grid(row=2, column=2)
    buttonSub = Button(frame, image=imagesub, width=100, height=100, command=lambda: calculator.simpleaction('sub'))
    buttonSub.grid(row=2, column=3)
    button0 = Button(frame, image=image0, width=100, height=100, command=lambda: calculator.addnumber(0))
    button0.grid(row=3, column=0)
    buttonDot = Button(frame, image=imagedot, width=100, height=100, command=lambda: calculator.isfloat())
    buttonDot.grid(row=3, column=1)
    buttonAdd = Button(frame, image=imageadd, width=100, height=100, calculator.simpleaction('add'))
    buttonAdd.grid(row=3, column=2)
    buttonEqu = Button(frame, image=imageequ, width=100, height=100, command=lambda: calculator.equal())
    buttonEqu.grid(row=3, column=3)

    window.mainloop()


if __name__ == '__main__':
    main()
