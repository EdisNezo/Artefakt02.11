from tkinter import *

import Conn
from ListboxSingleSelector import ListboxSingleSelector

sql_cmd = "SELECT name from sqlite_master"
column_name = 'name'


class ArchivedResults:

    def __init__(self, frame):
        self.mainFrame = ListboxSingleSelector(
            frame,
            'Archivierte Experimente',
            sql_cmd,
            column_name,
            Conn.connection_artefakt
        )
        self.closeBtn = Button(self.mainFrame.mainFrame, text="Schließen", command=self.mainFrame.mainFrame.destroy)
        self.closeBtn.pack(side=BOTTOM)

    def show(self):
        self.mainFrame.show()

    def hide(self):
        self.mainFrame.hide()
