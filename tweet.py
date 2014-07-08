import tweepy
CONSUMER_KEY = 'd9A58jFxpQURROph3St6g'
CONSUMER_SECRET ='tEaAKgazoS6ADKOFUSnHYPKRAXKiBSGAPnO2FS2szE'
OAUTH_TOKEN = '19491497-4jrBajpX0t2PHevDavyRnyJlkKpNjLwVx6YNBYgY0'
OAUTH_TOKEN_SECRET = 'KqUaDgn2RYfuGJx4b92qSsAn0qo38CCcMGRUpW1GlQ'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

api.update_status('twitting from python')
print 1
