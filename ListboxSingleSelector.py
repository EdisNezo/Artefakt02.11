from tkinter import *
from tkinter import ttk
import pandas as pd

import Conn
from ResultTable import ResultTable
from ResultTableAsToplevel import ResultTableAsToplevel


class ListboxSingleSelector:
    def __init__(self, frame, label_name, sql_insert, column_name, connection, toplevel=False, select_only=False):
        self.selected_indices = None
        if toplevel:
            self.mainFrame = Toplevel(frame)
            self.mainFrame.title(label_name)
            self.mainFrame.geometry("1000x800")
        else:
            self.mainFrame = Frame(frame)
            self.title = LabelFrame(self.mainFrame, text=label_name, labelanchor='n')
            self.title.pack(fill=BOTH, expand=True, pady=20, padx=20)

        table = pd.read_sql_query(sql_insert, connection)
        tableAsList = table[column_name].values.tolist()
        #print(tableAsList)
        tableAsListVar = Variable(value=tableAsList)
        self.listbox = Listbox(self.title, listvariable=tableAsListVar, height=40, width=150,
                               selectmode=SINGLE)
        self.listbox.pack(expand=True, fill=BOTH, side=LEFT)

        # scrollbar for listbox
        scrollbar = ttk.Scrollbar(
            self.listbox,
            orient=VERTICAL,
            command=self.listbox.yview
        )

        self.listbox['yscrollcommand'] = scrollbar.set
        scrollbar.pack(side=LEFT, expand=True, fill=Y)

        if select_only:
            self.listbox.bind('<<ListboxSelect>>', self.select_item)
        else:
            self.listbox.bind('<<ListboxSelect>>', self.select_item_and_open)

    def select_item(self, event):
        # get all selected indices
        self.selected_indices = str(self.listbox.get(ANCHOR))

    def select_item_and_open(self, event):
        # get all selected indices
        self.selected_indices = str(self.listbox.get(ANCHOR))
        self.openWindow(self.selected_indices)

    def openWindow(self, table_name):
        ResultTableAsToplevel(
            self.mainFrame,
            Conn.connection_artefakt,
            table_name,
            ResultTable.columns_for_exp
        )

    def show(self):
        self.mainFrame.pack(fill=BOTH, expand=True)

    def hide(self):
        self.mainFrame.pack_forget()
