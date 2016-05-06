## this harvest members from a twitter lists and puts them in a database for later harvesting
import tweepy
import keys
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user=keys.dbuser, password=keys.dbpass, database=keys.database)
cursor2 = mariadb_connection.cursor()

consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
access_token = keys.access_token
access_token_secret = keys.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

file = open("tweets.txt", "w")

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)


cursor2.execute("SELECT twithandle FROM foamites WHERE started=0 ORDER BY lastscraped ASC LIMIT 100") ##select 100 people who haven't yet been scraped
for row in cursor2:
    twitacct = row[0]
    for status in tweepy.Cursor(api.user_timeline, id=twitacct).items(1): # get a single tweet so start and max ids atsrt properly
        print status.text
        encodedtweet = unicode(status.text).encode('utf-8')
        tweetID = status.id
        max_id = tweetID - 1
        print tweetID
        print max_id
        file.write(encodedtweet)
        file.write("\n")
    #update with since_id, max_id and started

file.close()

#mariadb_connection.commit()
cursor2.close()
