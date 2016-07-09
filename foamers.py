import sqlite3
import csv

conn = sqlite3.connect('Scraper/foambot.sqlite')
cursor = conn.cursor()

#myfile = open('foamers.csv', 'wb')
#wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
print "about to query"
cursor.execute("SELECT twithandle, started FROM foamites LIMIT 10") ##select 100 people who haven't yet been scraped
print "query done"
for row in cursor:
    twithandle = row[0]
    started = row[1]

    print twithandle
    print started
    #wr.writerow(twithandle, started)
