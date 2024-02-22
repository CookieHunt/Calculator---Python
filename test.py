from tkinter import *
import math


def main():
    print('Hello World!')

    window = Tk()
    window.title('Calculator')
    window.geometry('400x600')

    icon = PhotoImage(file='icon.png')
    window.iconphoto(True, icon)

    window.mainloop()

    print('some buttons added here to check if new branch works :)')

    return 0


if __name__ == '__main__':
    main()
