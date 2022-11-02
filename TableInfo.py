import pandas as pd
import os

import Conn

sample = (
'C:/Users/EdisN/Desktop/Hausarbeit/sample/csvtest1.csv', 'C:/Users/EdisN/Desktop/Hausarbeit/sample/csvtest2.csv',
'C:/Users/EdisN/Desktop/Hausarbeit/sample/csvtest3.csv')


def checkIfTableExists(connection, table_name):
    cursor = connection.cursor_art()
    sql_stmt = "SELECT name FROM sqlite_master WHERE type='table' AND name = {}".format(table_name)
    listOfTables = cursor.execute(sql_stmt).fetchall()
    if not listOfTables:
        return True
    else:
        return False


class TableInfo:
    def __init__(self, files):
        self.tableInfo = []
        for path in files:
            if ".csv" in path:
                tablename = os.path.basename(path)
                tablename = os.path.splitext(tablename)[0]
                table = pd.read_csv(path, sep=';')
                table.to_sql(name=tablename, con=Conn.connection_csv, if_exists='replace')
                table['table_name'] = [tablename, tablename, tablename, tablename, tablename, tablename, tablename]
                self.tableInfo.append(table)
            else:
                tablename = path
                sql_cmd = "SELECT * FROM {}".format(tablename)
                table = pd.read_sql(sql_cmd, Conn.connection_csv)
                table['table_name'] = [tablename, tablename, tablename, tablename, tablename, tablename, tablename]
                self.tableInfo.append(table)

    def getTableAllInfo(self):
        return self.tableInfo

    def getTableInfo(self, index):
        return self.tableInfo[index]

    def getTableInfoColumn(self, table_index, column):
        return self.tableInfo[table_index][column]
