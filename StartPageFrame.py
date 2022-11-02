from tkinter import *
from tkinter import filedialog
from TableInfo import TableInfo


class StartPageFrame:

    def __init__(self, frame):
        self.status = False
        self.experimentName = None
        self.countTables = 0
        self.files = None
        self.actualFile = None
        self.repetitions = None
        self.startPageFrame = Frame(frame)

        Label(self.startPageFrame,
              text="Evaluationsplattform für haptische Kommunikation individueller Gefühlszustände",
              font=('Arial', '16', 'bold')).pack()

        self.experimentNameFrame = LabelFrame(self.startPageFrame, text="Erstellen Sie ein neues Experiment oder verwenden Sie ein bestehendes:")
        self.experimentNameFrame.pack(pady=20, padx=10, fill=BOTH)

        self.experimentNewBtn = Button(self.experimentNameFrame, text="Neues Experiment erstellen", bg='lightgrey')
        self.experimentNewBtn.pack(side=LEFT, padx=10)

        self.existingExperimentsBtn = Button(self.experimentNameFrame, text="Bestehendes Experiment verwenden", bg='lightgrey')
        self.existingExperimentsBtn.pack(side=LEFT, padx=10)

        self.selectTableLabelFrame = LabelFrame(self.startPageFrame,
                                                text="Wählen Sie die Emotionscodierung aus, die sie für dieses Experiment verwenden wollen:")
        self.selectTableLabelFrame.pack(pady=20, padx=10, fill=BOTH)

        # Button um Tabelle auszuwählen
        self.selectTableBtn = Button(self.selectTableLabelFrame, text="Emotionscodierung auswählen:", command=self.browseFiles)
        self.selectTableBtn.pack(fill=X, padx=10, pady=5)

        self.previousTablesBtn = Button(self.selectTableLabelFrame, text="Bereits importierte Emotionscodierung verwenden:")
        self.previousTablesBtn.pack(side=LEFT, padx=10)

        self.countTablesText = Label(self.selectTableLabelFrame,
                                     text="Anzahl der ausgewählten Tabellen: {}".format(self.countTables))
        self.countTablesText.pack(anchor="w", pady=5, padx=5)

        # Frame für Wiederholungen
        self.selectRepsFrame = LabelFrame(self.startPageFrame, text="Wählen Sie aus, wie viele Emotionen einer Tabelle benutzt werden sollen:")
        self.selectRepsFrame.pack(pady=20, padx=10, fill=BOTH)
        # Feld für Wiederholungen
        self.selectReps = Spinbox(self.selectRepsFrame, from_=1, to=100)
        self.selectReps.pack(fill=X, padx=10, pady=10)

        self.frame_for_start_and_auto_Btn = Frame(self.startPageFrame)
        self.frame_for_start_and_auto_Btn.pack()

        self.startBtn = Button(self.frame_for_start_and_auto_Btn, text="Manuellen Durchlauf starten", width=30, height=10, bd=4,
                               bg='lightgreen')
        self.startBtn.pack(side=LEFT, padx=5)

        self.automationBtn = Button(self.frame_for_start_and_auto_Btn, text="Automatisierten Durchlauf starten",
                                    width=30, height=10, bd=4,
                                    bg='lightgreen')
        self.automationBtn.pack(side=LEFT, padx=5)

        # Frame für archivierte Ergebnisse
        self.archivedResultsFrame = LabelFrame(self.startPageFrame)
        self.archivedResultsFrame.pack(side=BOTTOM, padx=15, pady=15)
        # Button für archivierte Ergebnisse
        self.archivedResultsBtn = Button(self.archivedResultsFrame, text="archivierte Ergebnisse", bd=4, bg='lightgrey')
        self.archivedResultsBtn.pack()

    def show(self):
        self.startPageFrame.pack(fill=BOTH, expand=True)
        self.setStatus(True)

    def hide(self):
        self.startPageFrame.pack_forget()
        self.setStatus(False)

    def updateRepetitions(self):
        self.repetitions = int(self.selectReps.get())
        print("Wiederholungen ausgewählt: " + str(self.repetitions))

    def browseFiles(self):
        self.files = filedialog.askopenfilenames(
            title="Tabellen auswählen",
            initialdir='/',
            filetypes=(
                ('Textdateien', '*.txt'),
                ('CSV-Dateien', '*.csv')
            )
        )
        self.changeCountTables(len(self.files))
        addedTablesWindow = Toplevel(self.startPageFrame)
        addedTablesWindow.title("Ausgewählte Tabellen")
        addedTablesWindow.geometry("700x500")
        Label(addedTablesWindow, text="Ausgewählten Tabellen:").pack()
        filesTemp = Variable(value=self.files)
        countTablesListbox = Listbox(addedTablesWindow, listvariable=filesTemp, height=6, selectmode=EXTENDED)
        countTablesListbox.pack(expand=True, fill=BOTH)
        Button(addedTablesWindow, text="Speichern", command=addedTablesWindow.destroy).pack()
        TableInfo(self.files)

    def setExperimentName(self, text):
        self.experimentName = text
        print("Experimente Name: " + str(self.experimentName))

    def updateActualFile(self, file):
        self.actualFile = file

    def setFiles(self, files):
        self.files = files

    def changeCountTables(self, count):
        self.countTables = count
        self.countTablesText.config(text="Anzahl der ausgewählten Tabellen: {}".format(self.countTables))

    def setStatus(self, bool):
        self.status = bool

    def getStatus(self):
        return self.status
