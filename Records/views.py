
# user pswrd - main

from django.http import HttpResponse
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PlayerSerializers
from .models import Players


# Create your views here.
def main(request):
    return HttpResponse('api/players-list')




@api_view(['GET'])
def playerlist(request):
    players = Players.objects.all()
    serializer = PlayerSerializers(players, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def playerdetail(request,pk):
    player = Players.objects.get(id = pk)
    serializer = PlayerSerializers(player, many = False)
    return Response(serializer.data)