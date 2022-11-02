from tkinter import *
from pandastable import Table
import pandas as pd

from ResultTable import ResultTable


class ResultTableAsFrame(ResultTable):
    def __init__(self, frame, connection, table_name, columns):
        self.mainFrame = Frame(frame)
        sql_query = pd.read_sql_query('SELECT * FROM {}'.format(table_name), connection)
        table_df = pd.DataFrame(sql_query, columns=columns)
        pt = Table(self.mainFrame, dataframe=table_df, editable=False)
        pt.show()

    def delete(self):
        self.mainFrame.destroy()

    def show(self):
        self.mainFrame.pack(expand=True, fill=BOTH)
