## this harvest members from a twitter lists and puts them in a database for later harvesting
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

## timer to stop us pissing off twitter too much
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print "hit API limit"
            time.sleep(15 * 60)

listslug = "foamed" #the name of the list
listowner = "ivorkovic" #name of the owner

for user in tweepy.Cursor(api.list_members, slug=listslug, owner_screen_name=listowner ).items(3200):
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

mariadb_connection.commit()
cursor2.close()
