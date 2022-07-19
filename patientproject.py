import csv

from cs50 import SQL #We are going to use this file to execute SQL Queries

open("patient.db", "w").close()

db = SQL("sqlite:///patient.db")

db.execute("CREATE TABLE doctor (Did INTEGER PRIMARY KEY AUTOINCREMENT, Dname TEXT, DPhone INTEGER,speciality TEXT )")         

db.execute("CREATE TABLE patient (Pid INTEGER PRIMARY KEY AUTOINCREMENT, Pname TEXT, PDOB REAL, Phone INTEGER )")

db.execute("CREATE TABLE Tests(Tid INTEGER, Cid INTEGER, Types TEXT, category TEXT, FOREIGN KEY(Tid) REFERENCES patient(Pid),FOREIGN KEY(Cid) REFERENCES doctor(Did))")
           
           
with open("patient.csv","r") as file:
    reader=csv.DictReader(file)
    
    for row in reader:
        
        Dname=row["Dname"]
        Speciality=row["Speciality"]
        Dphone=row["Dphone"]
        Tid=db.execute("INSERT INTO doctor(Dname,Dphone,Speciality) VALUES(?,?,?)",Dname,Dphone,Speciality)
        Pname=row["Pname"].strip().capitalize()
        PDOB=row["PDOB"]
        Phone=row["Phone"]
        Test_type=row["Test type"]
        Test_category=row["Test category"]
        man = db.execute("INSERT INTO patient(Pname,PDOB,Phone) VALUES(?,?,?)",Pname,PDOB,Phone)
        db.execute("INSERT INTO Tests(Tid,Cid,Types,category) VALUES((SELECT Pid FROM patient WHERE Pid =?),(SELECT Did FROM doctor WHERE Did =?),?,?)",man,Tid,Test_type,Test_category)
