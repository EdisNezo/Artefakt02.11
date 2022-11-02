from tkinter import *
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import matplotlib.pyplot as plt
import Conn


def getValues(exp_name, frame):
    y = []
    sql_insert = "SELECT table_name from {}".format(exp_name)
    used_tables_as_DataFrame = pd.read_sql_query(sql_insert, Conn.connection_usedTables)
    used_tables_as_list = used_tables_as_DataFrame['table_name'].values.tolist()
    not_used_table = []
    for elem in used_tables_as_list[:]:
        sql = "SELECT diff_emotion FROM " + exp_name + " WHERE table_name = '{}'".format(
            str(elem))
        diff_emotion_DataFrame = pd.read_sql_query(sql, Conn.connection_artefakt)
        diff_emotion_as_list = diff_emotion_DataFrame['diff_emotion'].values.tolist()
        print(elem)
        print(sum(diff_emotion_as_list))

        if diff_emotion_DataFrame.empty:
            not_used_table.append(elem)
            used_tables_as_list.remove(elem)
        else:
            y.append(sum(diff_emotion_as_list))

    print(used_tables_as_list)
    print(y)
    dic = {'Emotionscodierungen': used_tables_as_list,
           'Durchschnittliche Abweichung': y
           }
    dic_df = pd.DataFrame(dic)

    figure = plt.Figure(figsize=(6, 5), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, frame)
    chart_type.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    dic_df = dic_df[['Emotionscodierungen', 'Durchschnittliche Abweichung']].groupby('Emotionscodierungen').sum()
    dic_df.plot(kind='bar', legend=True, ax=ax)
    ax.set_title('Ergebnisse des Experiments')

    min_deviation = min(y)
    max_deviation = max(y)
    textFrame = Frame(frame)
    textFrame.pack(side=RIGHT, padx=15)
    # print(dic_df)
    if not_used_table is not []:
        for x in not_used_table:
            Label(textFrame,
                  text="Notiz: Die Tabelle {} wurde bei dem Experiment nicht benutzt, obwohl sie ausgewählt wurde".format(x)
                  ).pack()
    Label(frame,
          text="Die ")


class Ranking:
    def __init__(self, frame, exp_name):
        self.mainFrame = Toplevel(frame)
        self.mainFrame.title("Ausgewähltes Experiment: {}".format(exp_name))
        self.mainFrame.geometry("1200x800")
        getValues(exp_name, self.mainFrame)

    def hide(self):
        self.mainFrame.destroy()
