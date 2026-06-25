import sqlite3

DB_PATH = r"C:\Users\CAPACITI-JHB\OneDrive - UVU Africa\Desktop\ticket\tickets.db"

def get_connection():
    return sqlite3.connect(
        f"file:{DB_PATH}?mode=ro",
        uri=True
    )