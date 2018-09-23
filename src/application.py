from flask import Flask, request
import logging
from twitter_client import Twitter_Handler

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', filename='./app.log', filemode='w')

application = Flask(__name__)

twitter_api_handler = Twitter_Handler()

@application.route('/')
def test_server_online():
    return "Server is online"

@application.route('/authurl', methods=['GET'])
def get_authorization_url():
    return twitter_api_handler.get_authorization_url()

if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0', port=5000)