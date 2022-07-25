from curses import raw
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import random

@api_view(['GET'])
def tips(request):
    rawData = json.load(open("tips/json/data.json","r"))
    data = {"status":200, "result":rawData["results"][random.randint(1,len(rawData["results"]))]}

    return Response(data)