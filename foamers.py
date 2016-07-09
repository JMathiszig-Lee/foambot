import sqlite3
import csv

conn = sqlite3.connect('Scraper/foambot.sqlite')
c = conn.cursor()

myfile = open('foamers.csv', 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

c.execute("SELECT twithandle, started FROM foamites ") ##select 100 people who haven't yet been scraped
for row in c:
    twithandle = row[0]
    started = row[1]
    wr.writerow(twithandle, started)
