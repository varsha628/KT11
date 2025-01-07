import json
import logging

import requests

#logging.basicConfig(level=logging.DEBUG,   filename="result.log",filemode="w")

class Slackapi:
    def __init__(self):
         self.base_url = "https://slack.com/api"
         self.token ='xoxb-8246374622468-8243912002658-Cg2HQUj29HzlBZ3uoy9QOVKI'


    def get_conversations_list(self):
        endpoint = f"{self.base_url}/conversations.list"
        try:
            response = requests.get(endpoint, headers={'Authorization':f'Bearer {self.token}'})
            response.raise_for_status()
            data = response.json()
            if not data.get("ok"):
                logging.error(f"Error fetching conversations list: {data.get('error')}")
                return None
            logging.info("Successfully fetched conversations list.")
            return data.get("channels", [])
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
            return None
    get_conversations_list(1)
