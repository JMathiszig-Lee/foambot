import sqlite3
import csv

conn = sqlite3.connect('Scraper/foambot.sqlite')
cursor2 = conn.cursor()

#myfile = open('foamers.csv', 'wb')
#wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
cursor2.execute("SELECT twithandle, userkey FROM foamites WHERE started=0 ORDER BY lastscraped ASC LIMIT 10") ##select 100 people who haven't yet been scraped
for row in cursor2:
    twitacct = row[0]
    dbid = row[1]

    print twitacct
    print dbid
    #wr.writerow(twithandle, started)
