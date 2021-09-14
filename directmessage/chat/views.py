from typing import List
from django.core.checks import messages
from django.shortcuts import redirect, render
from chat.models import Chatroom, Message
from django.http import HttpResponse, JsonResponse
from datetime import datetime
# Create your views here.
def home(request):
    return render(request, 'index.html')

def room(request, room):
    username = request.GET.get('username')
    chatroom_details = Chatroom.objects.get(name = room)
    return render(request, 'chatroom.html',{
        'username': username,
        'room': room,
        'chatroom_details': chatroom_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Chatroom.objects.filter(name = room).exists():
        return redirect('/'+room+'/?username='+username)

    else:
        new_chatroom = Chatroom.objects.create(name = room)
        new_chatroom.save()
        return redirect('/'+room+'/?username='+username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(text = message, user = username, room = room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    chatroom_details = Chatroom.objects.get(name = room)
    messages = Message.objects.filter(room = chatroom_details.id)
    correctedMessages = changeDateOfMessages(messages)
    return JsonResponse({"messages": list(correctedMessages.values())})

def changeDateOfMessages(messages):
    for message in messages:
        message.date = datetime.strftime(message.date, '%Y-%m-%d %H:%M:%S')
    return messages