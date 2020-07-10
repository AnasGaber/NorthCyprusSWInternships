#!/Python/Python38/python
import cgi
import sqlite3
import webbrowser
import os
import http.cookies as Cookie
import string
import random
import time

def printHeader(title):

    print("Content-type: text/html")
    print("")
    print("<html><head><title>{}</title></head><body>".format(title))

def printFooter():
    print("</body></html>")

printHeader("Login")

form=cgi.FieldStorage()
username=form["un"].value
password=form["psw"].value

if "HTTP_COOKIE" in os.environ:
    cookie=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])

conn=sqlite3.connect("internship.db")
c=conn.cursor()

c.execute("SELECT password FROM companies WHERE username=?",(username,))
rows = c.fetchall()
if rows:
    if(rows[0][0]==password):
        cookie=Cookie.SimpleCookie()
        id=str(random.randint(1,1000000))
        for i in range(3):
            id=id+random.choice(string.ascii_letters)
        cookie["session"]=id
        cookie["session"]["domain"]="localhost"
        cookie["session"]["path"]="/"
        c.execute("UPDATE companies SET sessionID=? WHERE username=?",(id,username))
        conn.commit()
        print("""<meta http-equiv="refresh"  content="0; URL='http://localhost/northcyprusswinterns/slogin.html'"/>""")
    else:
        print("""<meta http-equiv="refresh"  content="0; URL='http://localhost/northcyprusswinterns/flogin.html'"/>""")
else:
        print("""<meta http-equiv="refresh"  content="0; URL='http://localhost/northcyprusswinterns/newuser.html'"/>""")
