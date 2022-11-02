from tkinter import *


class SurveyFrame:

    def __init__(self, frame):
        self.intensityScaleValue = None
        self.emotionScaleValue = None
        self.SurveyFrame = LabelFrame(frame)

        Label(self.SurveyFrame, text="Versuchsteilnehmer ist dran:", font=('Arial', '18', 'bold')).pack()
        Label(self.SurveyFrame,
              text="Schätzen Sie welche Emotion Sie durch das Wearable gespürt haben.",
              font=('Arial', '16')).pack()

        self.emotionScaleFrame = LabelFrame(self.SurveyFrame)
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

        self.rateEmotionBtn = Button(self.SurveyFrame, text="Emotion schätzen")
        self.rateEmotionBtn.pack(pady=15)

    def show(self):
        self.SurveyFrame.pack(expand=True, fill=BOTH)

    def hide(self):
        self.SurveyFrame.pack_forget()

    def getEmotion(self):
        self.emotionScaleValue = int(self.radio.get())

    def resetEmotion(self):
        self.radio.set(0)

