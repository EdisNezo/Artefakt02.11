from tkinter import *
import sqlite3
import pandas as pd
from pandastable import Table

import Conn
from ResultTable import ResultTable
from ResultTableAsFrame import ResultTableAsFrame


class ResultsFrame:
    def __init__(self, frame):
        self.resultTable = None
        self.table_df = None
        self.resultsTableFrame = None
        self.resultsPageFrame = LabelFrame(frame)

        self.resultsLabel = Label(self.resultsPageFrame, text="Ergebnisse")
        self.resultsLabel.pack()

        self.resetBtn = Button(self.resultsPageFrame, text="Zur Startseite")
        self.resetBtn.pack(side=BOTTOM)

    def show(self):
        self.resultsPageFrame.pack(fill=BOTH, expand=True)

    def hide(self):
        self.resultsPageFrame.pack_forget()

    def createResultTable(self, table):
        self.resultTable = ResultTableAsFrame(
            self.resultsPageFrame,
            Conn.connection_artefakt,
            table,
            ResultTable.columns_for_exp
        )

    def deleteCreatedResultTable(self):
        self.resultTable.delete()
