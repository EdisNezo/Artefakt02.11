import sqlite3

connection_artefakt = sqlite3.connect("artefakt.db", isolation_level=None)
connection_csv = sqlite3.connect("csv_tables.db", isolation_level=None)
connection_usedTables = sqlite3.connect("usedTables.db", isolation_level=None)
connection_participants = sqlite3.connect("participants.db", isolation_level=None)

cursor_art = connection_artefakt.cursor()
cursor_csv = connection_csv.cursor()
cursor_usedTables = connection_usedTables.cursor()
cursor_participants = connection_participants.cursor()
