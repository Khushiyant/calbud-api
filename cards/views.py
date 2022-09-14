from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

data = {
    'success': True
}

@api_view(['GET'])
def get_cards(request):
    return Response(data)

@api_view(['GET'])
def get_card(request, card_id):
    return Response(data)

@api_view(['POST'])
def create_card(request):
    return Response(data)

@api_view(['PUT'])
def update_card(request, card_id):
    return Response(data)

@api_view(['DELETE'])
def delete_card(request, card_id):
    return Response(data)

