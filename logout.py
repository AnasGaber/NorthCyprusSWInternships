#!/Python/Python38/python
import cgi
import sqlite3
import http.cookies as Cookie

def printHeader(title):

    print("Content-type: text/html")
    print("")
    print("<html><head><title>{}</title></head><body>".format(title))

def printFooter():
    print("</body></html>")

printHeader("Logout")
print("<p>here</p>")
conn=sqlite3.connect("internship.db")
c=conn.cursor()
c.execute("""UPDATE companies SET sessionID="-1" WHERE sessionID!="-1"""")
conn.commit()
print("""<meta http-equiv="refresh"  content="0; URL='http://localhost/northcyprusswinterns/index.html'"/>""")
printFooter()
