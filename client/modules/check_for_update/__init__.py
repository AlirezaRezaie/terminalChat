import requests
import json

END_POINT = "https://api.github.com/repos/AlirezaRezaie/terminalChat/tags"
AUTH_KEY = "token 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"


class Github:
    """  
       github api client that has methods 
       for accessing latest tags and commits
     """
    def __init__(self,endpoint,authkey):
        self.endpoint = endpoint
        self.authkey = authkey

    def get_last_tag(self) -> str:
        headers ={
            "Authoriztion": self.authkey,
        }

        latest_tag = requests.get(self.endpoint,headers=headers).content
        return json.loads(latest_tag.decode('utf-8'))[0]["name"]


def check_for_update(tag):
    print("Checking for update")
    needs_update = False
    api_client = Github(END_POINT,AUTH_KEY)
    if api_client.get_last_tag() != tag:
        needs_update = True
    elif needs_update:
        print("yala boro update kon 'git pull'")
    elif not needs_update: print("already up-to-date")