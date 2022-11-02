from tkinter import *
import sqlite3
import random
import pandas as pd

import Conn
import main
from tkinter import messagebox

from ArchivedExperiments import ArchivedExperiments
from ArchivedResults import ArchivedResults
from Countdown import Countdown
from EndScreen import EndScreen
from Instruction import Instruction
from ParticipantsFormular import ParticipantsFormular
from PreviousTables import PreviousTables
from Ranking import Ranking
from SelectArchivedResults import SelectArchivedResults
from TableInfo import TableInfo
from StartPageFrame import StartPageFrame
from SelectEmotionFrame import SelectEmotionFrame
from SurveyFrame import SurveyFrame
from ResultsFrame import ResultsFrame

auto = False
is_existing_experiment = False
passes = 0
participant = None


def createTable(table):
    # cursor.execute("DROP TABLE IF EXISTS {name}".format(name=table))
    Conn.cursor_art.execute('''CREATE TABLE IF NOT EXISTS {name}(
        'dg' INTEGER PRIMARY KEY,
        'correct_emotion' INTEGER,
        'guessed_emotion' INTEGER,
        'diff_emotion' INTEGER,
        'table_name' TEXT,
        'participant' INTEGER)'''.format(name=table))
    Conn.cursor_usedTables.execute(
        "CREATE TABLE IF NOT EXISTS {}('index' INTEGER PRIMARY KEY, 'table_name' TEXT)".format(table))
    Conn.cursor_participants.execute(
        """CREATE TABLE IF NOT EXISTS {name}(
         'index' INTEGER PRIMARY KEY,
         'age' TEXT,
         'gender' TEXT,
         'family_status' TEXT,
         'school_degree' TEXT,
         'employment' TEXT,
         'salary' TEXT)""".format(name=table)
    )


def insertValues(en, a, b, c, table_name, participant):
    # insert = "INSERT INTO {} ('correct_emotion', 'guessed_emotion', 'diff_emotion', 'table_name') VALUES(?, ?, ?, ?)".format(t, parameter)
    Conn.cursor_art.execute(
        "INSERT INTO " + en + "('correct_emotion', 'guessed_emotion', 'diff_emotion', 'table_name', 'participant') VALUES(?, ?, ?, ?, ?)",
        (a, b, c, table_name, participant))


def insertValues_for_usedTables(experiment_name, table_name):
    Conn.cursor_usedTables.execute(
        "INSERT INTO " + experiment_name + "('table_name') VALUES(?)",
        (table_name,))


def insertValues_for_participants(experiment_name, age, gender, family_status, school_degree, employment, salary):
    Conn.cursor_participants.execute(
        "INSERT INTO " + experiment_name + "('age', 'gender', 'family_status', 'school_degree', 'employment', 'salary') VALUES(?, ?, ?, ?, ?, ?)",
        (age, gender, family_status, school_degree, employment, salary)
    )


def manuel_startBtn_pressed(event):
    if StartPage.files is not None and StartPage.experimentName is not None and len(StartPage.experimentName) > 0:
        StartPage.hide()
        Instruction_Page.show()
    else:
        messagebox.showerror("Error",
                             "Bitte geben Sie einen Namen für das Experiment ein und wählen Sie Tabellen aus, die sie benutzen wollen!")


def sendEmotionBtn_pressed(event):
    if passes < StartPage.repetitions:
        SelectEmotion.hide()
        SelectEmotion.updateEmotion()
        countdown = Countdown(window, 3)
        countdown.start(Survey.show)
    else:
        print("Ende")


def guessEmotionBtn_pressed(event):
    main.passes += 1
    if main.auto and main.passes < StartPage.repetitions:
        countdown = Countdown(window, 3)
        countdown.start(autoSelectEmotion)
    else:
        SelectEmotion.show()
    Survey.hide()
    print("Durchlauf: " + str(main.passes))
    Survey.getEmotion()
    diffEmotion = diff(SelectEmotion.emotionScaleValue, Survey.emotionScaleValue)
    tableName = StartPage.actualFile.iloc[[SelectEmotion.emotionScaleValue - 1]]['table_name'].item()
    insertValues(
        StartPage.experimentName,
        SelectEmotion.emotionScaleValue,  # a
        Survey.emotionScaleValue,  # b
        diffEmotion,  # c
        tableName,  # table_name,
        participant
    )
    resetEmotions()
    if main.passes >= StartPage.repetitions:
        print("Ende")
        Survey.hide()
        SelectEmotion.hide()
        EndScreen_Page.createResultTable(StartPage.experimentName)
        EndScreen_Page.show()


def diff(a, b):
    return abs(a - b)


def getRandomTable(tables):
    StartPage.updateActualFile(random.choice(tables))


def ArchiveBtn_pressed(event):
    StartPage.hide()
    Archived_Experiments.show()


def CloseArchiveBtn_pressed():
    Archived_Experiments.hide()
    StartPage.show()


def existingExperimentsBtn_pressed():
    StartPage.hide()
    ExistingExp.show()


def previousTablesBtn_pressed():
    StartPage.hide()
    PreviousTab.show()


def resetEmotions():
    SelectEmotion.resetEmotion()
    Survey.resetEmotion()


def go_to_startpage():
    main.passes = 0
    resetEmotions()
    EndScreen_Page.hide_results()
    EndScreen_Page.hide()
    Archive.hide()
    StartPage.show()


def confirmExistingExp(event):
    def getTablesFromExp(exp_name):
        sql_insert = "SELECT * from {}".format(exp_name)
        table = pd.read_sql_query(sql_insert, Conn.connection_usedTables)
        tableAsList = table['table_name'].values.tolist()
        return list(dict.fromkeys(tableAsList))

    ExistingExp.hide()
    StartPage.setExperimentName(ExistingExp.returnSelectedItem())
    StartPage.show()
    if StartPage.experimentName is not None:
        StartPage.selectTableBtn.config(text="Tabelle bereits ausgewählt.", state=DISABLED)
        StartPage.previousTablesBtn.config(text="Tabelle bereits ausgewählt.", state=DISABLED)
        StartPage.setFiles(getTablesFromExp(StartPage.experimentName))
        StartPage.changeCountTables(len(StartPage.files))
        main.is_existing_experiment = True


def confirmPrevTab(event):
    PreviousTab.hide()
    StartPage.setFiles(PreviousTab.mainFrame.selected_indices)
    StartPage.changeCountTables(len(StartPage.files))
    StartPage.show()


def auto_startBtn_pressed(event):
    if StartPage.files is not None and StartPage.experimentName is not None and len(StartPage.experimentName) > 0:
        main.auto = True
        StartPage.hide()
        Instruction_Page.show()
    else:
        messagebox.showerror("Error",
                             "Bitte geben Sie einen Namen für das Experiment ein und wählen Sie Tabellen aus, die sie benutzen wollen!")


def autoSelectEmotion():
    if passes < StartPage.repetitions:
        SelectEmotion.getRandomEmotion()
        print("Zufällige Emotion ausgewählt!")
        Survey.show()
    else:
        print("Ende")


def newExperiment(event):
    temp = Toplevel(window)
    user_input = StringVar(window)

    def checkIfExists(text):
        sql_insert = "SELECT name from sqlite_master"
        column_name = 'name'
        table = pd.read_sql_query(sql_insert, Conn.connection_artefakt)
        tableAsList = table[column_name].values.tolist()

        if text in tableAsList:
            messagebox.showerror("Error",
                                 "Experiment besteht bereits! Wählen Sie einen neuen Namen oder wählen Sie ein bestehendes Experiment.")
        else:
            StartPage.setExperimentName(text)
            StartPage.selectTableBtn.config(text="Emotionscodierung auswählen:", state=NORMAL)
            StartPage.previousTablesBtn.config(text="Bereits importierte Emotionscodierung verwenden:", state=NORMAL)

    def changeExp(event):
        checkIfExists(user_input.get())

    temp.title("Neues Experiment erstellen")
    temp.geometry("400x100")
    Label(temp, text="Name des Experiments eingeben:").pack()
    tempEntry = Entry(temp, width=60, textvariable=user_input)
    tempEntry.pack(padx=5, pady=5)
    tempBtn = Button(temp, text="Bestätigen", command=temp.destroy)
    tempBtn.pack()
    tempBtn.bind("<Button>", changeExp)
    temp.focus()
    temp.grab_set()
    temp.mainloop()


def switch_page_from_introduction_to_participants1():
    Instruction_Page.hide()
    Participants_Page.show_page1()


def switch_page_from_participants1_to_participants2():
    Participants_Page.hide_page1()
    Participants_Page.show_page2()


def switch_page_from_participants2_to_participants1():
    Participants_Page.hide_page2()
    Participants_Page.show_page1()


def switch_page_from_participants2_to_START():
    if Participants_Page.are_checked():
        Participants_Page.hide_page2()
        startRun()
    else:
        messagebox.showerror("Error",
                             "Bitte füllen Sie alle benötigten Daten aus!")


def startRun():
    if len(StartPage.experimentName) > 0 and StartPage.files is not None:
        StartPage.updateRepetitions()
        createTable(StartPage.experimentName)
        insertValues_for_participants(
            experiment_name=StartPage.experimentName,
            age=Participants_Page.getAge(),
            gender=Participants_Page.getGender(),
            family_status=Participants_Page.getFamilyStatus(),
            school_degree=Participants_Page.getSchoolDegree(),
            employment=Participants_Page.getEmployment(),
            salary=Participants_Page.getSalary()
        )
        main.participant = getActualParticipant(StartPage.experimentName)
        print(participant)
        if not is_existing_experiment:
            for x in StartPage.files:
                insertValues_for_usedTables(StartPage.experimentName, x)
        getRandomTable(TableInfo(StartPage.files).getTableAllInfo())
        if main.auto:
            countdown = Countdown(window, 3)
            countdown.start(autoSelectEmotion)
        else:
            SelectEmotion.show()
    else:
        messagebox.showerror("Error",
                             "Bitte geben Sie einen Namen für das Experiment ein und wählen Sie Tabellen aus, die sie benutzen wollen!")


def getActualParticipant(exp_name):
    Conn.cursor_art.execute(
        "SELECT participant FROM {} ORDER BY dg DESC LIMIT 1".format(exp_name)
    )
    result = Conn.cursor_art.fetchone()
    if result is None:
        return 1
    else:
        return int(result[0]) + 1


def open_ranking_page():
    if Archived_Experiments.returnSelectedItem() is not None:
        Ranking(window, Archived_Experiments.returnSelectedItem())
    else:
        messagebox.showerror("Error",
                             "Bitte wählen Sie ein Experiment aus!")


def open_detail_page():
    if Archived_Experiments.returnSelectedItem() is not None:
        Archived_Experiments.openWindow(Archived_Experiments.returnSelectedItem())
    else:
        messagebox.showerror("Error",
                             "Bitte wählen Sie ein Experiment aus!")


window = Tk()
window.title("Design einer Evaluationsplattform für haptische Kommunikation individueller Gefühlszustände")
window.geometry("1400x800")

StartPage = StartPageFrame(frame=window)
StartPage.show()
SelectEmotion = SelectEmotionFrame(frame=window)
Survey = SurveyFrame(frame=window)
Results = ResultsFrame(frame=window)
Archive = ArchivedResults(frame=window)
ExistingExp = SelectArchivedResults(frame=window)
PreviousTab = PreviousTables(frame=window)
Archived_Experiments = ArchivedExperiments(frame=window)
Instruction_Page = Instruction(frame=window)
Participants_Page = ParticipantsFormular(frame=window)
EndScreen_Page = EndScreen(frame=window)

# Binding
StartPage.startBtn.bind("<Button>", manuel_startBtn_pressed)
StartPage.archivedResultsBtn.bind("<Button>", ArchiveBtn_pressed)
SelectEmotion.sendEmotionBtn.bind("<Button>", sendEmotionBtn_pressed)
Survey.rateEmotionBtn.bind("<Button>", guessEmotionBtn_pressed)
# Results.resetBtn.bind("<Button>", go_to_startpage)
PreviousTab.confirmBtn.bind("<Button>", confirmPrevTab)
ExistingExp.confirmBtn.bind("<Button>", confirmExistingExp)
# Archive.closeBtn.bind("<Button>", CloseArchiveBtn_pressed)
StartPage.automationBtn.bind("<Button>", auto_startBtn_pressed)
StartPage.experimentNewBtn.bind("<Button>", newExperiment)
# StartPage.selectTableBtn.bind("<Button>", StartPage.browseFiles)


StartPage.existingExperimentsBtn.config(command=existingExperimentsBtn_pressed)
StartPage.previousTablesBtn.config(command=previousTablesBtn_pressed)
Archived_Experiments.closeBtn.config(command=CloseArchiveBtn_pressed)
Instruction_Page.continueBtn.config(command=switch_page_from_introduction_to_participants1)
Participants_Page.continueBtn1.config(command=switch_page_from_participants1_to_participants2)
Participants_Page.continueBtn2.config(command=switch_page_from_participants2_to_START)
Participants_Page.backBtn2.config(command=switch_page_from_participants2_to_participants1)
EndScreen_Page.return_to_startpageBtn.config(command=go_to_startpage)
Archived_Experiments.rankingBtn.config(command=open_ranking_page)
Archived_Experiments.detailBtn.config(command=open_detail_page)
window.mainloop()
# Conn.connection_artefakt.close()
# Conn.connection_usedTables.close()
Conn.connection_participants.close()
# window.destroy()
