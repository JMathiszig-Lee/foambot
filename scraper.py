import tweepy
import keys

consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
access_token = keys.access_token
access_token_secret = keys.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

file = open("tweets.txt", "a")

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

twitacct = "707914932378079232"

for status in tweepy.Cursor(api.user_timeline, id=twitacct).items(5):
    print status.text
    encodedtweet = unicode(status.text).encode('utf-8')
    tweetID = status.id
    max_id = tweetID - 1
    print tweetID
    print max_id
    file.write(encodedtweet)
    file.write("\n")
    #process_status(status)

file.close()
