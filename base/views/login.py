from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import logout

def index(request):
    return JsonResponse({'test':"test"})


# Login 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token
 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
 

# Logout
def logout_request(request):
    print (request.user)
    logout(request)
    print (request.user)
    return JsonResponse({'LOGOUT':'SUCCESS'})


# Register
@api_view(['POST'])
def adduser(request):
    User.objects.create_user(username=request.data['username'], email=request.data['email'],
     password=request.data['password'],is_staff=0,is_superuser=True)
    return JsonResponse({'REGISTER':'SUCCESS'})


   