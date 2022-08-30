from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers

class Message(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    sender = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, related_name='sender')
    receiver = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, related_name='receiver')
    message = models.CharField(max_length=300,null=True,blank=True)
    subject = models.CharField(max_length=50,null=True,blank=True)
    read = models.BooleanField(default=False)
    createdTime = models.DateTimeField(auto_now_add=True)


class MessageSerializer(serializers.ModelSerializer):
    def getMessage(self,obj):
        return {
            "id"          : obj.id,
            "sender"      : str(obj.sender.username),
            "receiver"    : str(obj.receiver.username),
            "message"     : obj.message,
            "subject"     : obj.subject,
            "read"        : obj.read,
            "createdTime" : obj.createdTime
            }