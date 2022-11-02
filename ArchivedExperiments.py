from tkinter import *

import Conn
from TreeviewSelector import TreeviewSelector

sql_name_of_experiment = "SELECT name from sqlite_master"
sql_number_of_tables_used = "SELECT count(*) from "
sql_number_of_participants = "SELECT count(*) from "
sql_number_of_total_repetitions = "SELECT count(*) from "
column_name = 'name'


class ArchivedExperiments:

    def __init__(self, frame):
        self.mainFrame = TreeviewSelector(
            frame,
            'Archivierte Experimente',
            sql_name_of_experiment,
            column_name,
            Conn.connection_artefakt,
            select_only=True
        )
        self.rankingBtn = Button(self.mainFrame.mainFrame, text="Ranking")
        self.rankingBtn.pack()
        self.detailBtn = Button(self.mainFrame.mainFrame, text="Details")
        self.detailBtn.pack()

        self.closeBtn = Button(self.mainFrame.mainFrame, text="Schließen", command=self.mainFrame.mainFrame.destroy)
        self.closeBtn.pack(side=BOTTOM)

    def show(self):
        self.mainFrame.show()

    def hide(self):
        self.mainFrame.hide()

    def returnSelectedItem(self):
        return self.mainFrame.item_select("s")

    def openWindow(self, table_name):
        self.mainFrame.openWindow(table_name)
