#!/Python/Python38/python
import cgi
import sqlite3
import os
import http.cookies as Cookie
import time

def printHeader(title):

    print("Content-type: text/html")
    print("")
    print("""<html><head>
    <title>Company Details</title>
          <link rel="stylesheet" type="text/css" href="style.css"></head><body>""")
def printFooter():
    print("</body></html>")

printHeader("Company Details")
conn=sqlite3.connect("internship.db")
c=conn.cursor()
print("<form>")
print("""<div class="tablebox"><h1>Active in Gazimagusa</h1>""")
print("""<table class="content-table "><thead><tr><th>Company Name</th><th>Email</th><th>Phone Number</th><th>Website</th><th>City</th><th>Address</th></tr></thead>
<tbody>""")
c.execute("SELECT name,email,phone,website,city,address FROM companies WHERE name=?",())
rows = c.fetchall()
print("<td>{}</td>".format(rows))
print("</tr>")
print("""</tbody></table>""")
print("<br>")
print("</form>")
printFooter()
