#file to create database table
import sqlite3

sqlite_file = 'foambot.sqlite' #name of databasefile

#connect to the database (and create it)
conn = sqlite3.connect(sqlite_file)
c =  conn.cursor()

#sql to create the table
sqlite_command = """  
CREATE TABLE foamites(
userkey INTEGER PRIMARY KEY AUTO INCREMENT,
twithandle
twitterid
since_id
max_id
started
lastscraped
);"""

#create the table
c.execute(sqlite_command)


#commit changes and close connection
conn.commit()
conn.close()
