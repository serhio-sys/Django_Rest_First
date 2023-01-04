from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import ContactSerializer,UserSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthor
from rest_framework.decorators import action
from .models import *
import uuid
from rest_framework import viewsets



class ContactAPIView(views.APIView):
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def get(self, request,*args, **kwargs):
        alls = Contact.objects.all()
        return Response({"GET":"This is a get request!","data":ContactSerializer(alls,many=True).data})

    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        data = request.data
        if serializer.is_valid():
            rq = ContactSerializer(Contact.objects.create(
            name=request.data['name'],
            email=request.data['email'],
            message=request.data['message'],
            image = request.data['image'],
            user = request.user
        ))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
class ModernDetailAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    permission_classes = (IsAuthor,)
    serializer_class = ContactSerializer
    
#work with viewsets

class UserContactsViewSets(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAuthor,)
    
    
    @action(methods=['get'],detail=False)
    def images(self,request):
        image = ["http://"+request.META['HTTP_HOST']+im.image.url for im in self.get_queryset()]
        return Response({"images":image},status=status.HTTP_200_OK)
    
    @action(methods=['get'],detail=True)
    def user(self,request,pk):
        us = Contact.objects.get(pk=uuid.UUID(pk)).user
        return Response({"user":UserSerializer(us).data},status=status.HTTP_200_OK)
    
    @action(methods=['post'],detail=False)
    def createcontact(self,request,*args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        data = request.data
        if serializer.is_valid():
            rq = ContactSerializer(Contact.objects.create(
            name=request.data['name'],
            email=request.data['email'],
            message=request.data['message'],
            image = request.data['image'],
            user = request.user
        ))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    