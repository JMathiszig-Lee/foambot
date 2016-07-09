import sqlite3
import csv

conn = sqlite3.connect('foambot.sqlite')
c = conn.cursor()

myfile = open('foamers.csv', 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

c.execute("SELECT COUNT(*) FROM foamites")
number_of_rows=c.fetchone()
print number_of_rows

c.execute("SELECT twithandle, started FROM foamites LIMIT 10") ##select 100 people who haven't yet been scraped
for row in c:
    twithandle = row[0]
    started = row[1]

    print twithandle
    print started
    data = [twithandle, started]
    wr.writerow(data)
