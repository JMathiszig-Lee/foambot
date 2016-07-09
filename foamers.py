import sqlite3

conn = sqlite3.connect('Scraper/foambot.sqlite')
c = conn.cursor()

c.execute("SELECT COUNT(*) FROM foamites")
result = c.fetchone()
number_of_rows = result[0]
print (c.fetchall)
print number_of_rows

c.execute("SELECT * FROM foamites WHERE started=0 ")
not_started = c.rowcount
print not_started

c.execute("SELECT * FROM foamites WHERE started=1 ")
started = c.rowcount
print started
