import sqlite3

conn=sqlite3.connect('internship.db')
c=conn.cursor()

c.execute("""CREATE TABLE  IF NOT EXISTS companies (
	username	TEXT  PRIMARY KEY,
	password	TEXT NOT NULL,
	name	TEXT,
	email	TEXT,
	phone	TEXT,
	website	TEXT,
	city	TEXT,
	sessionID	TEXT,
	address	TEXT)""")

c.execute("""CREATE TABLE  IF NOT EXISTS cities (
	"cityID"	INTEGER DEFAULT 1 PRIMARY KEY AUTOINCREMENT,
	"cityname"	TEXT)""")

c.execute("""CREATE TABLE  IF NOT EXISTS internships (
	internshipID	INTEGER PRIMARY KEY AUTOINCREMENT,
	companyName TEXT,
	positioName	TEXT NOT NULL,
	description	TEXT,
	expectations TEXT,
	deadline	TEXT)""")

c.execute("INSERT INTO cities (cityname) VALUES('Gazimagusa')")
c.execute("INSERT INTO cities (cityname) VALUES('Girne')")
c.execute("INSERT INTO cities (cityname) VALUES('Guzelyurt')")
c.execute("INSERT INTO cities (cityname) VALUES('Iskele')")
c.execute("INSERT INTO cities (cityname) VALUES('Lefke')")
c.execute("INSERT INTO cities (cityname) VALUES('Lefkosa')")

conn.commit()
c.close()
conn.close()
