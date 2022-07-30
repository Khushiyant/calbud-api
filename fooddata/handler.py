import requests
import json

class handler:
    BASE_URL = "https://api.edamam.com/api/food-database/v2/parser"

    def __init__(self, app_id, app_key, food) -> None:
        if app_id == None or app_key == None:
            return

        self.params = {
            "app_id": app_id,
            "app_key": app_key,
            "ingr": food
        }
        self.processed_data = dict()
    
    def get_data(self) -> dict:
        try:
            r = requests.get(url=self.BASE_URL, params=self.params)
            data_dict = json.loads(r.text)

            raw_data = data_dict['parsed'][0]

            self.processed_data["nutrients"] = raw_data['food']["nutrients"]
            self.processed_data["image"] = raw_data['food']["image"]
            return self.processed_data
        except Exception as e:
            return {"status":400,"error":str(e)}

if __name__ == "__main__":
    from os import getenv
    print(handler(getenv("APP_ID"),getenv("APP_KEY"),'oats').get_data())