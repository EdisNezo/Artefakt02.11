from tkinter import *


class Countdown:
    def __init__(self, frame, count):
        self.count = count
        self.mainFrame = Frame(frame)
        self.countdownLabel = Label(self.mainFrame, text="", font=('Arial', '30', 'bold'))
        self.countdownLabel.pack(anchor=CENTER, pady=30)
        self.show()

    def show(self):
        self.mainFrame.pack(expand=True, fill=BOTH)

    def hide(self):
        self.mainFrame.destroy()

    def getCount(self):
        return self.count

    def setCount(self, count):
        self.count = count

    def start(self, func):
        self.countdownLabel.config(text=self.count)

        if self.count > 0:
            self.setCount(self.count-1)
            self.mainFrame.after(1000, self.start, func)
        else:
            self.hide()
            func()
