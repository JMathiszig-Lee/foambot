#file to create database table
import sqlite3

sqlite_file = 'Scraper/foambot.sqlite' #name of databasefile

#connect to the database (and create it)
conn = sqlite3.connect(sqlite_file)
c =  conn.cursor()

#sql to create the table
sqlite_command = """
    CREATE TABLE foamites(
    userkey INTEGER PRIMARY KEY,
    twithandle TEXT,
    twitterid INTEGER,
    since_id INTEGER,
    max_id INTEGER,
    started INTEGER DEFAULT 0 ,
    lastscraped NUMERIC DEFAULT CURRENT_TIMESTAMP);"""

#create the table
c.execute(sqlite_command)



#commit changes and close connection
conn.commit()
conn.close()
