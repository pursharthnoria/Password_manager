import sqlite3

def connect_master():
    conn = sqlite3.connect("passwords.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS master_password (name TEXT, password TEXT)")
    conn.commit()
    conn.close()

def view_master():
    conn = sqlite3.connect("passwords.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM master_password")
    rows = cur.fetchall()
    conn.close()
    return rows

def insert_master(name,password):
    conn = sqlite3.connect("passwords.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO master_password VALUES(?,?)",(name,password))
    conn.commit()
    conn.close()

def connect():
    conn = sqlite3.connect("passwords.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS passwords (website TEXT, password TEXT)")
    conn.commit()
    conn.close()

def insert(website,password):
    conn = sqlite3.connect("passwords.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO passwords VALUES(?,?)",(website,password))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("passwords.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM passwords")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(website):
    conn = sqlite3.connect("passwords.db")
    cur = conn.cursor()
    cur.execute("SELECT password FROM passwords WHERE website=?",(website,))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(website):
    conn = sqlite3.connect("passwords.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM passwords WHERE website=?",(website,))
    conn.commit()
    conn.close()