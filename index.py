#!/Python/Python38/python


def printHeader(title):
    print("Content-type: text/html")
    print("")
    print("<html><head><title>{}</title></head><body>".format(title))

def printFooter():
    print("</body></html>")


printHeader("NCI")
print("""<meta http-equiv="refresh"  content="0; URL='http://localhost/northcyprusswinterns/index.html'"/>""")


printFooter()
