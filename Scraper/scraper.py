## main scraper
import tweepy
import keys
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user=keys.dbuser, password=keys.dbpass, database=keys.database)
cursor2 = mariadb_connection.cursor(buffered=True) #buffer select query or you'll get unread erros
cursor3 = mariadb_connection.cursor() #unbuffered for update as otherwise it only updates the first row


consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
access_token = keys.access_token
access_token_secret = keys.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

file = open("tweets.txt", "a") #using append rather then write so we don't delete our hard work

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

numtweets = 0
cursor2.execute("SELECT twithandle, userkey, since_id, max_id FROM foamites WHERE started=1 ORDER BY lastscraped ASC LIMIT 40") ##select 40 people who have gone through the start script
for row in cursor2:
    twitacct = row[0]
    dbid = row[1]
    sinceid = row[2]
    maxid = row[3]

    for status in tweepy.Cursor(api.user_timeline, id=twitacct, max_id=maxid).items(80): # get 80 tweets (3200 limit)
        tweet = status.text
        tweet = tweet.replace('\n','') #strip out all the line breaks that make text file horrible

        encodedtweet = unicode(tweet).encode('utf-8') #encode tweet so it writes to the txt file
        file.write(encodedtweet)
        file.write("\n")

        tweetID = status.id

        if tweetID > sinceid: #probably don't need this bit as since_id seems to be broken
            sinceid = tweetID

        elif tweetID < maxid:
            maxid = tweetID - 1

    #update with since_id, max_id and started


        try:
            cursor3.execute("UPDATE foamites SET since_id = %s, max_id = %s, started = 1, lastscraped = CURRENT_TIMESTAMP WHERE userkey = %s ", (sinceid, maxid, dbid,))
        except mariadb.Error as error:
            print("Error: {}".format(error))
        global numtweets
        numtweets += 1

print numtweets
file.close()
mariadb_connection.commit()
cursor2.close()
cursor3.close()
