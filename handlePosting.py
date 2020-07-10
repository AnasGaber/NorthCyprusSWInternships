#!/Python/Python38/python
import cgi
import sqlite3

def printHeader(title):
    print("Content-type: text/html")
    print("")
    print("<html><head><title>{}</title></head><body>".format(title))

def printFooter():
    print("</body></html>")

printHeader("Form")

form=cgi.FieldStorage()
position=form["position"].value
detail=form["positiondesc"].value
expect=form["expect"].value
deadline=form["deadline"].value

conn=sqlite3.connect("internship.db")
c=conn.cursor()

c.execute("SELECT name FROM companies WHERE sessionID<>?",(str(-1),))
comname=c.fetchone()

c.execute("INSERT INTO internships (companyName,positioName,description,expectations,deadline) VALUES (?,?,?,?,?)",(comname[0],position,detail,expect,deadline))
conn.commit()

print("""<meta http-equiv="refresh"  content="0; URL='http://localhost/northcyprusswinterns/newintern.html'"/>""")
