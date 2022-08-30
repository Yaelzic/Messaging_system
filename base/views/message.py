from asyncore import read
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from ..models import Message, MessageSerializer
from django.db.models import Q
from django.shortcuts import get_object_or_404

# Get messages
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def messages(request, id=-1):
    user = request.user 
    if int(id) > -1: # read selected message
        try:
            message = Message.objects.get(id=id)
            res = MessageSerializer().getMessage(message)
            message.read = True
            message.save()
        except:
            return JsonResponse({'Error':' message matching query does not exist.'})       
        return JsonResponse(res)   
    res = []  # show all messages per user
    for messageObj in Message.objects.filter(Q(sender=user)|Q(receiver=user)):
                res.append(MessageSerializer().getMessage(messageObj)) 
    return JsonResponse(res,safe=False) 


# Get unread messages
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def unread(request, id=-1):
    user = request.user 
    res = []  # show unread messages per user
    unreadMess = []
    for messageObj in Message.objects.filter(Q(sender=user)|Q(receiver=user)):
                res.append(MessageSerializer().getMessage(messageObj)) 
    unreadMess = [message for message in res if message['read'] == False]
    return JsonResponse(unreadMess, safe=False)     


# Add new message
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def newmessage(request):
    try:
        receiver = User.objects.get(email=request.data['receiver'])
    except:
        return JsonResponse({'Error':' user matching query does not exist.'}) 
    message = request.data['message']
    subject = request.data['subject']
    Message.objects.create(sender=request.user,receiver=receiver,message=message,subject=subject)
    return JsonResponse({'POST':'SUCCESS'})


# Delete message 
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delmessage(request, id):
    message = Message.objects.get(id=id)
    message.delete()
    return JsonResponse ({'DELETE': 'SUCCESS'})

