from tkinter import *
import Conn
from ListboxMultiSelector import ListboxMultiSelector

label_name = "Gespeicherte Tabellen"
sql_cmd = "SELECT name from sqlite_master WHERE type='table'"
column_name = 'name'


class PreviousTables:
    def __init__(self, frame):
        self.mainFrame = ListboxMultiSelector(
            frame,
            label_name,
            sql_cmd,
            column_name,
            Conn.connection_csv,
            select_only=True
        )
        self.confirmBtn = Button(self.mainFrame.mainFrame, text="Bestätigen", command=self.mainFrame.mainFrame.destroy)
        self.confirmBtn.pack(side=BOTTOM)

    def show(self):
        self.mainFrame.show()

    def hide(self):
        self.mainFrame.hide()
