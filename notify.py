import os

from dotenv import load_dotenv
from linebot.v3 import messaging  # type: ignore

load_dotenv(override=True)


def main():
    access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    configuration = messaging.Configuration(access_token=access_token)  # noqa


if __name__ == "__main__":
    main()
