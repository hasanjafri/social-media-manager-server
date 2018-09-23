from flask import Flask, request, redirect
import logging
from twitter_client import Twitter_Handler

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', filename='./app.log', filemode='w')

application = Flask(__name__)

twitter_api_handler = Twitter_Handler()

@application.route('/')
def test_server_online():
    return "Server is online"

@application.route('/twitter/getVerifier', methods=['GET'])
def get_verifier():
    return redirect(twitter_api_handler.get_authorization_url())

@application.route('/twitter/getAccessToken', methods=['GET'])
def get_access_token_and_secret():
    return twitter_api_handler.get_access_token_and_secret()

if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0', port=5000)