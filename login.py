import cgi
import sqlite3
from bottle import route, run, template, static_file, request, redirect
import urllib
import re


@route('/submitLoginForm', method='POST')
def user_login():
   username = form["un"].value
   password = form["psw"].value
   conn = sqlite3.connect("intership.db")
   cursor = conn.cursor()
   the_data = list(cursor.execute('SELECT userName, password from softwarecompany'))
   if username in the_data:
        return open('mainmenu.html').read()
   else:
        return "<p>credentials invalid </p>"
