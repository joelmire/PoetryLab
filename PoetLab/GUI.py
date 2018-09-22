'''
Created on Aug 14, 2017

@author: joelmire
'''
from Tkinter import *
from lab import *


def filterSelection():
    constructor = Tk()
    frame = Frame(constructor)
    frame.pack()

    button1 = Button(frame, text = 'noun', command = filterSearch('N'))
    button2 = Button(frame, text = 'Button 2')
    button3 = Button(frame, text = 'Button 3')
    button4 = Button(frame, text = 'Button 4')

    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()

    constructor.mainloop()







if __name__ == '__main__':
    