import sqlite3

#backend

def passengerData():
    con = sqlite3.connect('passenger.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS passenger(id INTEGER PRIMARY KEY, PsgID text,Firstname text,Surname text,DoB text,Age text,Gender text,Address text,Mobile text)")
    con.commit()
    con.close()

def addStdRec(PsgID,Firstname,Surname,DoB,Age,Gender,Address,Mobile):
    con = sqlite3.connect('passenger.db')
    cur = con.cursor()
    cur.execute("INSERT INTO passenger VALUES(NULL,?,?,?,?,?,?,?,?)",(PsgID,Firstname,Surname,DoB,Age,Gender,Address,Mobile))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect('passenger.db')
    cur = con.cursor()
    cur.execute("Select * FROM passenger")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con = sqlite3.connect('passenger.db')
    cur = con.cursor()
    cur.execute("DELETE FROM passenger WHERE id = ?",(id,))
    con.commit()
    con.close()

def searchData(PsgID = "",Firstname = "",Surname = "",DoB = "",Age = "",Gender = "",Address = "",Mobile = ""):
    con = sqlite3.connect("passenger.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM passenger WHERE PsgID = ? OR Firstname = ? OR Surname = ? OR DoB = ? OR Age = ? OR Gender =? OR Address =? OR Mobile = ?", (PsgID,Firstname,Surname,DoB,Age,Gender,Address,Mobile))
    rows = cur.fetchall()
    con.close()
    return rows

def dataUpdate(id,PsgID = "",Firstname = "",Surname = "",DoB = "",Age = "",Gender = "",Address = "",Mobile = ""):
    con = sqlite3.connect("passenger.db")
    cur = con.cursor()
    cur.execute("UPDATE passenger SET PsgID = ?,Firstname = ?, Surname = ?, DoB = ?, Age = ?, Gender =?,Address =?, Mobile = ?,WHERE id = ?",(PsgID, Firstname, Surname, DoB, Age, Gender, Address, Mobile,id))
    con.commit()
    con.close()


passengerData()
