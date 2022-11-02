from tkinter import *


class ParticipantsFormular:
    def __init__(self, frame):
        self.mainFrame1 = Frame(frame)

        self.ageFrame = LabelFrame(self.mainFrame1, text="Alter")
        self.ageFrame.pack()
        Label(self.ageFrame, text="Zu welcher der nachfolgenden Alterskategorien gehören Sie?",
              font=('Arial', '11', 'bold')).pack(pady=5)

        self.ageVar = StringVar(value=' ')

        Radiobutton(self.ageFrame, value="17 oder jünger", variable=self.ageVar, text="17 oder jünger").pack()
        Radiobutton(self.ageFrame, value="18-20", variable=self.ageVar, text="18-20").pack()
        Radiobutton(self.ageFrame, value="21-29", variable=self.ageVar, text="21-29").pack()
        Radiobutton(self.ageFrame, value="30-39", variable=self.ageVar, text="30-39").pack()
        Radiobutton(self.ageFrame, value="40-49", variable=self.ageVar, text="40-49").pack()
        Radiobutton(self.ageFrame, value="50-59", variable=self.ageVar, text="50-59").pack()
        Radiobutton(self.ageFrame, value="60 oder älter", variable=self.ageVar, text="60 oder älter").pack()

        self.genderFrame = LabelFrame(self.mainFrame1, text="Geschlecht")
        self.genderFrame.pack()
        Label(self.genderFrame, text="Bitte geben Sie Ihr Geschlecht an.", font=('Arial', '11', 'bold')).pack(pady=5)

        self.genderVar = StringVar(value=' ')

        Radiobutton(self.genderFrame, value="M", variable=self.genderVar, text="Männlich").pack()
        Radiobutton(self.genderFrame, value="W", variable=self.genderVar, text="Weiblich").pack()
        Radiobutton(self.genderFrame, value="D", variable=self.genderVar, text="Divers").pack()

        self.family_statusFrame = LabelFrame(self.mainFrame1, text="Familienstand")
        self.family_statusFrame.pack()

        Label(self.family_statusFrame,
              text="Sind Sie derzeit verheiratet, verwitwet, geschieden, getrennt oder ledig?",
              font=('Arial', '11', 'bold')).pack(pady=5)
        self.family_statusVar = StringVar(value=' ')

        Radiobutton(self.family_statusFrame, value="Verheiratet", variable=self.family_statusVar,
                    text="Verheiratet").pack()
        Radiobutton(self.family_statusFrame, value="Verwitwet", variable=self.family_statusVar, text="Verwitwet").pack()
        Radiobutton(self.family_statusFrame, value="Geschieden", variable=self.family_statusVar,
                    text="Geschieden").pack()
        Radiobutton(self.family_statusFrame, value="Getrennt", variable=self.family_statusVar, text="Getrennt").pack()
        Radiobutton(self.family_statusFrame, value="Ledig", variable=self.family_statusVar, text="Ledig").pack()

        self.school_degreeFrame = LabelFrame(self.mainFrame1, text="Schulabschluss")
        self.school_degreeFrame.pack()

        Label(self.school_degreeFrame, text="Was ist Ihr höchster Schul- oder Hochschulabschluss?",
              font=('Arial', '11', 'bold')).pack(pady=5)
        self.school_degreeVar = StringVar(value=' ')

        Radiobutton(self.school_degreeFrame, value="Unterer Schulabschluss", variable=self.school_degreeVar,
                    text="Unterer Schulabschluss").pack()
        Radiobutton(self.school_degreeFrame, value="Abitur oder gleichwertiger Abschluss",
                    variable=self.school_degreeVar,
                    text="Abitur oder gleichwertiger Abschluss").pack()
        Radiobutton(self.school_degreeFrame, value="Studium ohne Abschluss", variable=self.school_degreeVar,
                    text="Studium ohne Abschluss").pack()
        Radiobutton(self.school_degreeFrame, value="Bachelor-Abschluss", variable=self.school_degreeVar,
                    text="Bachelor-Abschluss").pack()
        Radiobutton(self.school_degreeFrame, value="Master-Abschluss", variable=self.school_degreeVar,
                    text="Master-Abschluss").pack()
        Radiobutton(self.school_degreeFrame, value="Doktor-Grad", variable=self.school_degreeVar,
                    text="Doktor-Grad").pack()

        self.continueBtn1 = Button(self.mainFrame1, text="Weiter")
        self.continueBtn1.pack(side=BOTTOM, pady=10, padx=10)

        self.mainFrame2 = Frame(frame)

        self.employmentFrame = LabelFrame(self.mainFrame2, text="Erwerbstätigkeit")
        self.employmentFrame.pack()

        Label(self.employmentFrame,
              text="Welche der folgenden Kategorien beschreibt Ihren Beschäftigungsstatus am besten?",
              font=('Arial', '11', 'bold')).pack(pady=5)
        self.employmentVar = StringVar(value=' ')

        Radiobutton(self.employmentFrame, value="Angestellt, Wochenarbeitszeit von 1-39 Stunden",
                    variable=self.employmentVar,
                    text="Angestellt, Wochenarbeitszeit von 1-39 Stunden").pack()
        Radiobutton(self.employmentFrame, value="Angestellt, Wochenarbeitszeit von 40 Stunden oder mehr",
                    variable=self.employmentVar,
                    text="Angestellt, Wochenarbeitszeit von 40 Stunden oder mehr").pack()
        Radiobutton(self.employmentFrame, value="Ohne Beschäftigung, arbeitssuchend", variable=self.employmentVar,
                    text="Ohne Beschäftigung, arbeitssuchend").pack()
        Radiobutton(self.employmentFrame, value="Ohne Beschäftigung, NICHT arbeitssuchend", variable=self.employmentVar,
                    text="Ohne Beschäftigung, NICHT arbeitssuchend").pack()
        Radiobutton(self.employmentFrame, value="Pensioniert", variable=self.employmentVar,
                    text="Pensioniert").pack()
        Radiobutton(self.employmentFrame, value="Behindert, arbeitsunfähig", variable=self.employmentVar,
                    text="Behindert, arbeitsunfähig").pack()

        self.salaryFrame = LabelFrame(self.mainFrame2, text="Haushaltseinkommen")
        self.salaryFrame.pack()

        Label(self.salaryFrame,
              text="Wie hoch war das gesamte Einkommen aller Mitglieder Ihres Haushalts im Jahr 2010?",
              font=('Arial', '11', 'bold')).pack(pady=5)
        self.salaryVar = StringVar(value=' ')

        Radiobutton(self.salaryFrame, value="0 – 9.999 EUR", variable=self.salaryVar,
                    text="0 – 9.999 EUR").pack()
        Radiobutton(self.salaryFrame, value="10.000 – 19.999 EUR",
                    variable=self.salaryVar,
                    text="10.000 – 19.999 EUR").pack()
        Radiobutton(self.salaryFrame, value="20.000 – 29.999 EUR", variable=self.salaryVar,
                    text="20.000 – 29.999 EUR").pack()
        Radiobutton(self.salaryFrame, value="30.000 – 39.999 EUR", variable=self.salaryVar,
                    text="30.000 – 39.999 EUR").pack()
        Radiobutton(self.salaryFrame, value="40.000 – 49.999 EUR", variable=self.salaryVar,
                    text="40.000 – 49.999 EUR").pack()
        Radiobutton(self.salaryFrame, value="50.000 – 59.999 EUR", variable=self.salaryVar,
                    text="50.000 – 59.999 EUR").pack()
        Radiobutton(self.salaryFrame, value="60.000 – 69.999 EUR", variable=self.salaryVar,
                    text="60.000 – 69.999 EUR").pack()
        Radiobutton(self.salaryFrame, value="70.000 – 79.999 EUR", variable=self.salaryVar,
                    text="70.000 – 79.999 EUR").pack()
        Radiobutton(self.salaryFrame, value="80.000 – 89.999 EUR", variable=self.salaryVar,
                    text="80.000 – 89.999 EUR").pack()
        Radiobutton(self.salaryFrame, value="90.000 – 99.999 EUR", variable=self.salaryVar,
                    text="90.000 – 99.999 EUR").pack()
        Radiobutton(self.salaryFrame, value="100.000 EUR oder mehr", variable=self.salaryVar,
                    text="100.000 EUR oder mehr").pack()

        self.backBtn2 = Button(self.mainFrame2, text="Zurück")
        self.backBtn2.pack(side=BOTTOM, pady=10, padx=10)

        self.continueBtn2 = Button(self.mainFrame2, text="Bestätigen")
        self.continueBtn2.pack(side=BOTTOM, pady=10)

    def getAge(self):
        return self.ageVar.get()

    def getGender(self):
        return self.genderVar.get()

    def getFamilyStatus(self):
        return self.family_statusVar.get()

    def getSchoolDegree(self):
        return self.school_degreeVar.get()

    def getEmployment(self):
        return self.employmentVar.get()

    def getSalary(self):
        return self.salaryVar.get()

    def show_page1(self):
        self.mainFrame1.pack(fill=BOTH, expand=True)

    def hide_page1(self):
        self.mainFrame1.pack_forget()

    def show_page2(self):
        self.mainFrame2.pack(fill=BOTH, expand=True)

    def hide_page2(self):
        self.mainFrame2.pack_forget()

    def are_checked(self):
        if self.getAge() == ' ' or self.getGender() == ' ' or self.getFamilyStatus() == ' ' or self.getSchoolDegree() == ' ' or self.getEmployment() == ' ' or self.getSalary() == ' ':
            return False
        else:
            return True
