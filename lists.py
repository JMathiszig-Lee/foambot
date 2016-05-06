import tweepy
import keys
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user=keys.dbuser, password=keys.dbpass, database=keys.database)
cursor2 = mariadb_connection.cursor()


query = ("SELECT twithandle FROM foamites WHERE twithandle=%s")

consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
access_token = keys.access_token
access_token_secret = keys.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)


for user in tweepy.Cursor(api.list_members, slug="foamed", owner_screen_name="sandnsurf" ).items(5):
    print user.screen_name
    print user.id
    twitterid = user.id
    twittername = user.screen_name

    cursor2.execute(query, (twittername,))
    row = cursor2.fetchone()
    if row is not None:
        print "in db"
    else:
        try:
            cursor2.execute("INSERT INTO foamites ( twithandle, twitterid ) VALUES (%s, %s) ",(twittername, twitterid))
            print "inserted"
        except mariadb.Error as error:
            print("Error: {}".format(error))
    encodedtweet = unicode(user.screen_name).encode('utf-8')

mariadb_connection.commit()
cursor2.close()
