from dotenv import load_dotenv
import os
from slack_bolt.app import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

def main():
    load_dotenv()

    slack_app_token = os.getenv("SLACK_APP_TOKEN")
    slack_bot_token = os.getenv("SLACK_BOT_TOKEN")

    app = App(token=slack_bot_token)

    handler = SocketModeHandler(app, slack_app_token)
    handler.start()

if __name__ == "__main__":
    main()