#!/Python/Python38/python
import cgi
import sqlite3
import time
def printHeader(title):
    print("Content-type: text/html")
    print("")
    print("<html><head><title>{}</title></head><body>".format(title))

def printFooter():
    print("</body></html>")

printHeader("Form")

form=cgi.FieldStorage()
username=form["usrname"].value
email=form["email"].value
companyName=form["companyName"].value
phoneNumber=form["phoneNumber"].value
password=form["psw"].value
website=form["website"].value
postalAdr=form["postalAdr"].value
cityind=form["city"].value
conn=sqlite3.connect("internship.db")
c=conn.cursor()
c.execute("SELECT cityname FROM cities WHERE cityID=?",cityind)
city=c.fetchall()
c.execute("INSERT INTO companies (username,password,name,email,phone,website,city,address) VALUES (?,?,?,?,?,?,?,?)",(username,password,companyName,email,phoneNumber,website,city[0][0],postalAdr))
conn.commit()
print("""<meta http-equiv="refresh"  content="0; URL='http://localhost/northcyprusswinterns/loginre.html'"/>""")
