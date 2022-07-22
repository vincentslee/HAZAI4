import time
import requests
import os
import json


class RequestMethod:
    get = 'get'
    post = 'post'
    put = 'put'


class Main:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def discord_api_request(self, method: str, endpoint: str, headers: dict = None, params: dict = None,
                            payload: dict = None) -> dict:
        url = self.kwargs['discord_base_url'] + endpoint
        if headers is None:
            headers = {
                "Authorization": f"Bot {self.kwargs['DISCORD_TOKEN']}"
            }
        else:
            headers["Authorization"] = f"Bot {self.kwargs['DISCORD_TOKEN']}"

        response = requests.request(method, url, headers=headers, params=params, json=payload)

        if response.status_code != 200:
            raise ValueError(response.text)
        else:
            return json.loads(response.text)

    def download_guild_member_data(self, guild_id) -> None:
        params = {
            "limit": "1000"
        }

        member_data = self.discord_api_request(RequestMethod.get, f"/guilds/{guild_id}/members", params=params)

        root_dir = os.path.dirname(os.path.abspath(__file__))
        with open(f"/{root_dir}/data/metadata/user_data.json", "w") as f:
            json.dump(member_data, f)
            f.close()

    def download_channel_message_history(self, channel_id) -> None:

        def get_messages(message_id=None):
            time.sleep(0.1)

            params = {
                "limit": "100"
            }

            if last_message_id is not None:
                params["before"] = message_id

            return self.discord_api_request(RequestMethod.get, f"/channels/{channel_id}/messages", params=params)

        root_dir = os.path.dirname(os.path.abspath(__file__))
        try:
            message_archive = json.load(open(f"{root_dir}/data/chatlogs/{channel_id}.json"))
            message_ids = list(message_archive.keys())
            message_history = get_messages(message_ids[-1])
        except Exception as e:
            print(e)
            message_archive = {}
            message_history = get_messages()

        reach_end = False
        while reach_end is False:
            for message in message_history:
                msg_id = message["id"]

                msg_obj = {
                    "content": message.get("content"),
                    "author": message.get("author").get("id"),
                    "attachments": message.get("attachments"),
                    "embeds": message.get("embeds"),
                    "timestamp": message.get("timestamp"),
                    "referenced_message": message.get("referenced_message").get("id") if message.get(
                        "referenced_message") else None,
                    "mentions": message.get("mentions"),
                    "reactions": message.get("reactions"),

                }

                message_archive[msg_id] = msg_obj

            with open(f"/{root_dir}/data/chatlogs/{channel_id}.json", "w") as f:
                json.dump(message_archive, f)
                f.close()

            if len(message_history) < 100:
                reach_end = True
            else:
                last_message_id = list(message_archive.keys())[-1]
                message_history = get_messages(last_message_id)
