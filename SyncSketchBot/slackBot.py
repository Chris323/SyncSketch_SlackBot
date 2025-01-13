from dotenv import load_dotenv
import os
from slack_bolt.app import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import requests


class SlackBot:
    def __init__(self):
        load_dotenv()

        #Slack Bot Api tokens
        self.slack_app_token = os.getenv("SLACK_APP_TOKEN")
        self.slack_bot_token = os.getenv("SLACK_BOT_TOKEN")

        #Slack Webhook URL
        self.webhook_url = os.getenv("WEBHOOK_URL")


    def start_bot(self):
        app = App(token=self.slack_bot_token)
        handler = SocketModeHandler(app, self.slack_app_token)
        handler.start()
    
    #AKA reverse api
    def send_webhook(self, input):
        text = "Hello Hammer Creative"
        payload = {"text" : text}
        requests.post(self.webhook_url, json=payload)
    
#Test
# slacky = SlackBot()
# slacky.send_webhook()