from tkinter import *


class Instruction:
    def __init__(self, frame):
        self.mainFrame = Frame(frame)
        self.instructions_LabelFrame = LabelFrame(self.mainFrame, text="Belehrung zum Experiment")
        self.instructions_LabelFrame.pack(fill=BOTH, expand=True)

        Label(self.instructions_LabelFrame,
              text="""Einwilligungserklärung gemäß Datenschutz
              für eine Umfrage zum Thema 'Evaluationsplattform für haptische Kommunikation individueller Gefühlszustände'""",
              font=('Arial', '12', 'bold')).pack()

        Label(self.instructions_LabelFrame,
              text="""
                Auf den folgenden Seiten wollen wir Ihnen ein paar Fragen stellen zum Thema “Evaluationsplattform für haptische Kommunikation individueller Gefühlszustände”.
                Ziel unserer Umfrage ist, den Nutzen von haptischen Kommunikationen individueller Gefühlszustände besser bewerten zu können.
                Am Anfang der Umfrage wollen wir zudem nähere Informationen zu Ihrer Person abfragen, 
                um dadurch bei den Ergebnissen auch soziale Faktoren (Alter, Berufsstand, Wohnverhältnisse) einzubeziehen und so die Bewertung verbessern zu können.
                Die Teilnahme an dieser Umfrage ist ohne die Nennung Ihres Namens möglich.
                Eine Registrierung ist für die Teilnahme nicht erforderlich.
                Auch bei einer Umfrage haben Sie gemäß Datenschutz gegenüber dem Informationsträger das Recht auf Auskunft sowie Löschung Ihrer personenbezogenen Daten. 
                Sie können diese Einwilligungserklärung jederzeit widerrufen. 
                Nutzen Sie hierzu dieses Formular https://www.verbraucherzentrale.de/sites/default/files/2019-10/Widerruf_der_Einwilligung_und_Loeschung_der_Daten.pdf.
                Nach erfolgtem Widerruf werden Ihre Daten gelöscht und unzugänglich aufbewahrt.
                """,
              font=('Arial', '11')).pack()

        self.continueBtn = Button(self.instructions_LabelFrame, text="Ich habe den Informationstext gelesen, bin einverstanden und möchte an der Umfrage teilnehmen.", font=('Arial', '14', 'bold'))
        self.continueBtn.pack()

    def show(self):
        self.mainFrame.pack(fill=BOTH, expand=True)

    def hide(self):
        self.mainFrame.pack_forget()

