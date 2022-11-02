from tkinter import *

import Conn
from ResultTable import ResultTable
from ResultTableAsFrame import ResultTableAsFrame


class EndScreen:
    def __init__(self, frame):
        self.temp = None
        self.mainFrame = Frame(frame)

        self.return_to_startpageBtn = Button(self.mainFrame, text="Zur Startseite")
        self.return_to_startpageBtn.pack(anchor='center')

        self.see_results = Button(self.mainFrame, text="Ergebnisse des Experiments ansehen",
                                  command=self.show_results)
        self.see_results.pack(anchor='center')

    def createResultTable(self, table):
        self.temp = ResultTableAsFrame(
            self.mainFrame,
            Conn.connection_artefakt,
            table,
            ResultTable.columns_for_exp
        )

    def show_results(self):
        self.temp.show()

    def hide_results(self):
        self.temp.delete()

    def show(self):
        self.mainFrame.pack(fill=BOTH, expand=True)

    def hide(self):
        self.mainFrame.pack_forget()
