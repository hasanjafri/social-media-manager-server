import tweepy
from auth import consumer_token, consumer_secret

class Twitter_Handler(object):
    def __init__(self):
        self.auth = tweepy.OAuthHandler(consumer_token, consumer_secret)

    def get_authorization_url(self):
        try:
            authorization_url = self.auth.get_authorization_url()
        except tweepy.TweepError as e:
            return("Error \n %s" % (e))
        return authorization_url

