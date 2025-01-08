from dotenv import load_dotenv
import os
from slack_bolt.app import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


class SlackBot:
    def __init__(self):
        load_dotenv()

        self.slack_app_token = os.getenv("SLACK_APP_TOKEN")
        self.slack_bot_token = os.getenv("SLACK_BOT_TOKEN")


    def start_connection(self):
        app = App(token=self.slack_bot_token)
        handler = SocketModeHandler(app, self.slack_app_token)
        handler.start()
    
#Test
# slacky = SlackBot()
# slacky.start_connection()