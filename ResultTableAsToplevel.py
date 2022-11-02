from tkinter import *
from pandastable import Table
import pandas as pd
from ResultTable import ResultTable


class ResultTableAsToplevel(ResultTable):
    def __init__(self, frame, connection, table_name, columns):
        self.mainWindow = Toplevel(frame)
        self.mainWindow.title("Ausgewähltes Experiment: {}".format(table_name))
        self.mainWindow.geometry("1000x800")

        sql_query = pd.read_sql_query('SELECT * FROM {}'.format(table_name), connection)
        table_df = pd.DataFrame(sql_query, columns=columns)
        pt = Table(self.mainWindow, dataframe=table_df, editable=False)
        pt.show()

    def delete(self):
        self.mainWindow.destroy()
