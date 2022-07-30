from email.charset import BASE64
import bs4
import requests
import json

class handler:
    BASE_URL = "https://api.edamam.com/api/food-database/v2/parser"

    def __init__(self, app_id, app_key, food) -> None:
        params = {
            "app_id": app_id,
            "app_key": app_key,
            "ingr": food
        }
        r = requests.get(url=self.BASE_URL, params=params)
        data_dict = json.loads(r.text)

        raw_data = data_dict['parsed'][0]

        self.processed_data = dict()
        self.processed_data["nutrients"] = raw_data['food']["nutrients"]
        self.processed_data["image"] = raw_data['food']["image"]
    
    def get_data(self) -> dict:
        return self.processed_data

if __name__ == "__main__":
    from os import getenv
    handler(getenv("APP_ID"),getenv("APP_KEY"),'oats')