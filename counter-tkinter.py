from tkinter import *

class Counter:
    def __init__(self):
        window = Tk()
        window.title('Counter')
        window.geometry('300x200')

        self.count = IntVar()
        self.count.set(0)
        
        self.lb_count = Label(window, textvariable=self.count, fg='blue')
        self.bt_inc = Button(window, text='Increment', command=self.increment, bg='cyan', cursor='plus')
        self.bt_dec = Button(window, text='Decrement', command=self.decrement, bg='yellow', cursor='circle')
        self.bt_reset = Button(window, text='Reset', command=self.reset, bg='pink')

        self.lb_count.pack()
        self.bt_inc.pack()
        self.bt_dec.pack()
        self.bt_reset.pack()

        window.mainloop()

    def reset(self):
        self.count.set(0)

    def increment(self):
        self.count.set(self.count.get()+1)
        
    def decrement(self):
        self.count.set(self.count.get()-1)

if (__name__ == '__main__'):
    Counter()