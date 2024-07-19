from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from django.contrib.auth.models import User
from user.api.serializers import UserSerializer
from user.api.permissions import isAdminUserOrReadOnly
from rest_framework import generics

class users_list_api_view(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [isAdminUserOrReadOnly]

class users_detail_api_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [isAdminUserOrReadOnly]





"""
class users_list_api_view(APIView):
    def get(self, request):
        users = User.objects.filter(is_active=  True)
        serializer = UserSerializer(users, many= True)
        return ( Response(serializer.data) )
    
    def post(self, request):
        serializer = UserSerializer(request.data)
        if (serializer.is_valid()):
            serializer.save()
            return (Response(serializer.data, status=status.HTTP_201_CREATED))
        return(Response(status=status.HTTP_400_BAD_REQUEST))
    
class users_detail_api_view(APIView):
    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)
    
    def get(self, request, pk):
        user_instance = self.get_object(pk)
        serializer = UserSerializer(user_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        user_instance = self.get_object(pk)  
        serializer = UserSerializer(user_instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        user_instance = self.get_object(pk)
        user_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""