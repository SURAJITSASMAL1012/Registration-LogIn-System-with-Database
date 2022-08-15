import sqlite3

def create_db():
    con=sqlite3.connect(database="RMS.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY AUTOINCREMENT,f_name text,l_name text,contact text,email text,question text,answer text,password text)")
    con.commit()
    con.close()

create_db()