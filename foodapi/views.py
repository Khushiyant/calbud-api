import os

import dotenv
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .fooddata import handler


def config():
    dotenv.load_dotenv()


APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")


@api_view(["GET"])
def food(request, ingr):
    data = handler.handler(APP_ID, APP_KEY, ingr).get_data()
    return Response(data)
