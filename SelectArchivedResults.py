from tkinter import *

import Conn
from TreeviewSelector import TreeviewSelector

sql_cmd = "SELECT name from sqlite_master"
column_name = 'name'


class SelectArchivedResults:

    def __init__(self, frame):
        self.mainFrame = TreeviewSelector(
            frame, 'Archivierte Experimente',
            sql_cmd,
            column_name,
            Conn.connection_artefakt,
            select_only=True
        )
        self.confirmBtn = Button(self.mainFrame.mainFrame, text="Bestätigen", command=self.mainFrame.mainFrame.destroy)
        self.confirmBtn.pack(side=BOTTOM)

    def show(self):
        self.mainFrame.show()

    def hide(self):
        self.mainFrame.hide()

    def returnSelectedItem(self):
        return self.mainFrame.item_select("s")
