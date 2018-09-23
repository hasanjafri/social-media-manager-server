import tweepy
from auth import consumer_token, consumer_secret, access_token, access_token_secret
from models.user import User
import json
import requests
import os
class Twitter_Handler(object):
    def __init__(self):
        self.auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
        self.temp_request_token = {}

    def get_authorization_url(self):
        try:
            authorization_url = self.auth.get_authorization_url()
        except tweepy.TweepError as e:
            return("Error! Failed to get request token. \n %s" % (e))

        self.temp_request_token = self.auth.request_token
        print(self.temp_request_token)
        return authorization_url

    def get_access_token_and_secret(self):
        self.auth.request_token = self.temp_request_token
        print(self.auth.request_token)
        verifier = input('Please enter the verification code: ')
        try:
            access = self.auth.get_access_token(verifier)
        except tweepy.TweepError as e:
            return("Error! Failed to get access token for user. \n %s" % (e))

        return("Worked, access_token: {}, access_secret: {}".format(access[0], access[1]))

    def get_self_info(self):
        self.auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(self.auth)
        me = api.me()
        return str(me)

    def get_all_followers(self):
        friends_list = []
        self.auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(self.auth)
        for friend in tweepy.Cursor(api.followers).items():
            friends_list.append(friend.screen_name + ':' + friend.id_str)
        return json.dumps(friends_list)

    def update_status(self, status="This was tweeted with Python bitches @AArulparan"):
        self.auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(self.auth)
        try:
            api.update_status(status)
        except tweepy.TweepError as e:
            return("Error! Failed to send direct message. \n %s" % (e))

        return "You tweeted {}".format(status)

    def update_status_with_media(self):
        self.auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(self.auth)
        filename = 'temp.jpg'
        request = requests.get('https://media.licdn.com/dms/image/C5603AQF8kuwkEMxQ0A/profile-displayphoto-shrink_800_800/0?e=1543449600&v=beta&t=EJOGr81rKHEcia7tGvdvN-AJB-IX0PKZJF5j0a9HRHA', stream=True)
        if request.status_code == 200:
            with open(filename, 'wb') as image:
                for chunk in request:
                    image.write(chunk)

            try:
                api.update_with_media(filename=filename, status="Trying to tweet with a photo attached programmatically @AArulparan")
                os.remove(filename)
            except tweepy.TweepError as e:
                return("Error! Failed to send direct message. \n %s" % (e))

            return "You tweeted with a photo attached!"
        else:
            return "Error! Unable to download image"

    def send_direct_message(self):
        self.auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(self.auth)
        try:
            return str(api.send_direct_message(user_id='621918163', text='This was sent with python bitch'))
        except tweepy.TweepError as e:
            return("Error! Failed to send direct message. \n %s" % (e))


