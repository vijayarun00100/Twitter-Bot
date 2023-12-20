import tweepy 
import time

authorisation = tweepy.OAuthHandler('xxxxxxxxxxxxxxxxxxxxxxxxx')
authorisation.set_access_token('xxxxxxxxxxxxxxxxxxxxxxxxx') 

api = tweepy.API(authorisation) 
user = api.me()
print(user.name)
# generous bot 
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next() 
    except tweepy.RateLimitError:
        time.sleep(1000) 

for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'vijay':
        follower.follow()
        break
    print(follower.name)  


search_string = 'thanking' 
numberOfTweets = 2 

for tweet in tweepy.Cursor(api.search,search_string).items(numberOfTweets):
    try:
        tweet.favorite() 
        print('I liked that tweet') 
    except tweepy.TweepError as err:
        print(err.reason) 
    except StopIteration:
        break



