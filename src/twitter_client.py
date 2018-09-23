import tweepy
from auth import consumer_token, consumer_secret

temp_request_token = {}
verifier =

class Twitter_Handler(object):
    def __init__(self, **kwargs):
        self.auth = tweepy.OAuthHandler(consumer_token, consumer_secret)

    def get_authorization_url(self):
        try:
            authorization_url = self.auth.get_authorization_url()
        except tweepy.TweepError as e:
            return("Error! Failed to get request token. \n %s" % (e))

        temp_request_token = self.auth.request_token
        return authorization_url

    def get_access_token_and_secret(self):
        self.auth.request_token = request_token
        return self.auth.get_access_token(verifier)
        

