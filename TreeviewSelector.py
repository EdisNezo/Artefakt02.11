from tkinter import *
from tkinter import ttk
import pandas as pd

import Conn
from Ranking import Ranking
from ResultTable import ResultTable
from ResultTableAsToplevel import ResultTableAsToplevel


class TreeviewSelector:
    def __init__(self, frame, label_name, sql_insert, column_name, connection, toplevel=False,
                 select_only=False):
        self.selected_indices = None
        if toplevel:
            self.mainFrame = Toplevel(frame)
            self.mainFrame.title(label_name)
            self.mainFrame.geometry("1000x800")
        else:
            self.mainFrame = Frame(frame)
            self.title = LabelFrame(self.mainFrame, text=label_name, labelanchor='n')
            self.title.pack(fill=BOTH, expand=True, pady=20, padx=20)

        self.tree = ttk.Treeview(self.title, height=30, show='headings', columns=("1", "2", "3", "4", "5"))

        self.tree.column("1", width=250, anchor='c')
        self.tree.column("2", width=200, anchor='c')
        self.tree.column("3", width=200, anchor='c')
        self.tree.column("4", width=200, anchor='c')

        self.tree.heading("1", text='Experiment Name')
        self.tree.heading("2", text='Anzahl der Emotionscodierung')
        self.tree.heading("3", text='Anzahl Teilnehmer')
        self.tree.heading("4", text='Anzahl Wiederholungen insgesamt des Experiments')

        experiment_names_as_DataFrame = pd.read_sql_query(sql_insert, connection)
        experiment_names_as_list = experiment_names_as_DataFrame[column_name].values.tolist()

        for name in experiment_names_as_list:
            sql_count = "SELECT count(*) from {}".format(name)

            number_of_tables_used_as_DataFrame = pd.read_sql_query(sql_count,
                                                                   Conn.connection_usedTables)
            number_of_tables_used = number_of_tables_used_as_DataFrame['count(*)'].values[0]

            number_of_participants_as_DataFrame = pd.read_sql_query(sql_count,
                                                                    Conn.connection_participants)  # !!!!!
            number_of_participants = number_of_participants_as_DataFrame['count(*)'].values[0]
            number_of_total_repetitions_as_DataFrame = pd.read_sql_query(sql_count,
                                                                         Conn.connection_artefakt)
            number_of_total_repetitions = number_of_total_repetitions_as_DataFrame['count(*)'].values[0]

            self.tree.insert('', END, iid=None, values=(name, number_of_tables_used, number_of_participants, number_of_total_repetitions))
        if select_only:
            self.tree.bind('<<TreeviewSelect>>', self.item_select)
        else:
            self.tree.bind('<<TreeviewSelect>>', self.item_select_and_open)
        self.tree.grid(row=0, column=0, sticky='nsew')

    def show(self):
        self.mainFrame.pack(fill=BOTH, expand=True)

    def hide(self):
        self.mainFrame.pack_forget()

    def item_select(self, event):
        for selected_item in self.tree.selection():
            curItem = self.tree.focus()
            column_data = self.tree.item(curItem)
            experiment_name = self.tree.item(curItem)['values'][0]
            number_of_tables_used = self.tree.item(curItem)['values'][1]
            number_of_participants = self.tree.item(curItem)['values'][2]
            number_of_total_repetitions = self.tree.item(curItem)['values'][3]
            return experiment_name

    def item_select_and_open(self, event):
        for selected_item in self.tree.selection():
            curItem = self.tree.focus()
            column_data = self.tree.item(curItem)
            experiment_name = self.tree.item(curItem)['values'][0]
            number_of_tables_used = self.tree.item(curItem)['values'][1]
            number_of_participants = self.tree.item(curItem)['values'][2]
            number_of_total_repetitions = self.tree.item(curItem)['values'][3]
            self.openWindow(experiment_name)

    def openWindow(self, table_name):
        ResultTableAsToplevel(
            self.mainFrame,
            Conn.connection_artefakt,
            table_name,
            ResultTable.columns_for_exp
        )
