import sqlite3

conn = sqlite3.connect('Scraper/foambot.sqlite')
c = conn.cursor()

c.execute("SELECT COUNT(*) * from foamites")
result = c.fetchone()

number_of_rows = result[0]

print number_of_rows
