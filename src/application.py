from flask import Flask, request, redirect
import logging
from twitter_client import Twitter_Handler
from instagram_client import Instagram_Handler

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', filename='./app.log', filemode='w')

application = Flask(__name__)

twitter_api_handler = Twitter_Handler()
instagram_api_handler = Instagram_Handler()

@application.route('/')
def test_server_online():
    return "Server is online"

@application.route('/twitter/getVerifier', methods=['GET'])
def get_verifier():
    return redirect(twitter_api_handler.get_authorization_url())

@application.route('/twitter/getAccessToken', methods=['GET'])
def get_access_token_and_secret():
    return twitter_api_handler.get_access_token_and_secret()

@application.route('/twitter/myInfo', methods=['GET'])
def get_self_info():
    return twitter_api_handler.get_self_info()

@application.route('/twitter/allFollowers', methods=['GET'])
def get_all_followers():
    return twitter_api_handler.get_all_followers()

@application.route('/twitter/directMessage', methods=['GET'])
def send_direct_message():
    return twitter_api_handler.send_direct_message()

@application.route('/twitter/updateStatus', methods=['GET'])
def update_status():
    return twitter_api_handler.update_status()

@application.route('/twitter/updateMediaStatus', methods=['GET'])
def update_status_with_media():
    return twitter_api_handler.update_status_with_media()

@application.route('/instagram/uploadPhoto', methods=['GET'])
def upload_photo_to_instagram():
    return instagram_api_handler.upload_photo()

if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0', port=5000)