import sqlite3

conn = sqlite3.connect('Scraper/foambot.sqlite')
c = conn.cursor()

c.execute("SELECT COUNT(*), * FROM foamites")
result = c.fetchone()

number_of_rows = result[0]

print len(c.fetchall)

print number_of_rows
