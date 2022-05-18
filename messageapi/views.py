import json
import io
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Message
from .serializers import MessageSerializer, UserSerializer, MessageDetailSerializer
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes, api_view


@csrf_exempt
@permission_classes((AllowAny,))
def signup(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = UserSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json.dumps({'message': 'user created successfully! now you can signin'}))
        else:
            return HttpResponse(json.dumps(serializer.errors))
    else:
        return HttpResponse('Only POST method is allowed')


@api_view(['POST'])
@csrf_exempt
def sendmessage(request):
    if request.method == 'POST':
        json_data = request.body
        token_data = request.headers['Authorization']
        token_data = token_data.split(' ')
        token_data = token_data[1]
        token = Token.objects.get(key=token_data)
        user = token.user
        messages = Message.objects.filter(
            created_by=user.id, created_at__gt=datetime.datetime.utcnow()-datetime.timedelta(hours=1)).count()
        if messages >= 10:
            return HttpResponse(json.dumps({'message': 'you have reached the limit of sending messages'}))
        else:
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            message = python_data['message']
            serializer = MessageSerializer(
                data={'message': message, 'created_by': user.id})
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(json.dumps({'message': 'message sent successfully!'}))
            else:
                return HttpResponse(json.dumps(serializer.errors))

    else:
        return HttpResponse('Only POST method is allowed')


@api_view(['GET'])
def getmessages(request):
    if request.method == 'GET':
        token_data = request.headers['Authorization']
        token_data = token_data.split(' ')
        token_data = token_data[1]
        token = Token.objects.get(key=token_data)
        user = token.user
        messages = Message.objects.filter(created_by=user.id)
        serializer = MessageDetailSerializer(messages, many=True)
        return HttpResponse(JSONRenderer().render(serializer.data))
