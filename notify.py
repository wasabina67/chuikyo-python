import os

from dotenv import load_dotenv
from linebot.v3 import messaging  # type: ignore

load_dotenv(override=True)


def main():
    access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    configuration = messaging.Configuration(access_token=access_token)
    num = "第596回"
    text = f"{num} の資料が公開されました。https://www.mhlw.go.jp/stf/shingi/shingi-chuo_128154.html"
    message_dict = {
        "messages": [
            {"type": "text", "text": text},
        ],
    }

    with messaging.ApiClient(configuration=configuration) as client:
        messaging_api = messaging.MessagingApi(client)
        broadcast_request = messaging.BroadcastRequest.from_dict(obj=message_dict)

        try:
            resp = messaging_api.broadcast(broadcast_request)  # noqa
            # print(resp)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
