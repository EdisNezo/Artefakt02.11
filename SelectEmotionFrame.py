import random
from tkinter import *


class SelectEmotionFrame:

    def __init__(self, frame):
        self.emotionScaleValue = None
        self.selectEmotionFrame = LabelFrame(frame)

        self.emotionTableLabel = Label(self.selectEmotionFrame,
                                       text="Versuchsleiter ist dran:", font=('Arial', '18', 'bold'))
        self.emotionTableLabel.pack()

        Label(self.selectEmotionFrame,
              text="Wählen Sie eine Emotion aus, die Sie dem Versuchsteilnehmer senden wollen.", font=('Arial', '16')).pack()

        self.emotionScaleFrame = LabelFrame(self.selectEmotionFrame)
        self.emotionScaleFrame.pack(fill=BOTH)

        self.radio = IntVar()

        Scale1 = PhotoImage(file=r"C:\Users\EdisN\Desktop\Hausarbeit\Artefakt\images\scale1.png")
        Scale2 = PhotoImage(file=r"C:\Users\EdisN\Desktop\Hausarbeit\Artefakt\images\2.png")
        Scale3 = PhotoImage(file=r"C:\Users\EdisN\Desktop\Hausarbeit\Artefakt\images\3.png")
        Scale4 = PhotoImage(file=r"C:\Users\EdisN\Desktop\Hausarbeit\Artefakt\images\4.png")
        Scale5 = PhotoImage(file=r"C:\Users\EdisN\Desktop\Hausarbeit\Artefakt\images\5.png")
        Scale6 = PhotoImage(file=r"C:\Users\EdisN\Desktop\Hausarbeit\Artefakt\images\6.png")
        Scale7 = PhotoImage(file=r"C:\Users\EdisN\Desktop\Hausarbeit\Artefakt\images\7.png")

        self.r1 = Radiobutton(self.emotionScaleFrame, value=1, variable=self.radio, image=Scale1)
        self.r1.image = Scale1
        self.r1.pack()
        self.r2 = Radiobutton(self.emotionScaleFrame, value=2, variable=self.radio, image=Scale2)
        self.r2.image = Scale2
        self.r2.pack()
        self.r3 = Radiobutton(self.emotionScaleFrame, value=3, variable=self.radio, image=Scale3)
        self.r3.image = Scale3
        self.r3.pack()
        self.r4 = Radiobutton(self.emotionScaleFrame, value=4, variable=self.radio, image=Scale4)
        self.r4.image = Scale4
        self.r4.pack()
        self.r5 = Radiobutton(self.emotionScaleFrame, value=5, variable=self.radio, image=Scale5)
        self.r5.image = Scale5
        self.r5.pack()
        self.r6 = Radiobutton(self.emotionScaleFrame, value=6, variable=self.radio, image=Scale6)
        self.r6.image = Scale6
        self.r6.pack()
        self.r7 = Radiobutton(self.emotionScaleFrame, value=7, variable=self.radio, image=Scale7)
        self.r7.image = Scale7
        self.r7.pack()

        self.sendEmotionBtn = Button(self.selectEmotionFrame, text="Emotion versenden")
        self.sendEmotionBtn.pack(pady=15)

    def show(self):
        self.selectEmotionFrame.pack(fill=BOTH, expand=True)

    def hide(self):
        self.selectEmotionFrame.pack_forget()

    def updateEmotion(self):
        self.emotionScaleValue = int(self.radio.get())

    def resetEmotion(self):
        self.radio.set(0)

    def setEmotionScaleValue(self, value):
        self.emotionScaleValue = int(value)

    def getRandomEmotion(self):
        ran = int(random.uniform(1, 7))
        self.setEmotionScaleValue(ran)

