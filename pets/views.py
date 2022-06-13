from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from pets.serializers import PetsSerializer
from pets.serializers import LoginSerializer
from pets.serializers import UserSerializer
from pets.models import Pets
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from rest_framework.decorators import api_view,permission_classes


# Create your views here.

class ListPetsAPIView(ListAPIView):
 # add permission to check if user is authenticated
    permission_classes = (permissions.AllowAny,)
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer
    
    # 1. List all
    def get(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        serializer = PetsSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

        
    #  3. GetById
class GetPetById(APIView):

    def getObject(self, request, pet_id, *args, **kwargs):
        '''
        Retrieves the Pet with given pet_id
        '''

        Pet_instance = Pets.objects.filter(pk=self.kwargs['pet_id'])
        if not Pet_instance:
            return Response(
                {"res": "Object with Pet id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PetsSerializer(Pet_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
class CreatePet(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        '''
        Create the Pets with given Pets data
        '''

        data = {
            'nom': request.data.get('nom'), 
            'prenom': request.data.get('prenom'), 
            'age': request.data.get('age'), 
            'descr': request.data.get('desc'), 
            'user': request.user.id
        }
        serializer = PetsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# class PetDetailApiView(APIView):
#     # add permission to check if user is authenticated
    

#     # 3. Retrieve
#     def get(self, request, pet_id, *args, **kwargs):
#         '''
#         Retrieves the Pet with given pet_id
#         '''
#         Pet_instance = self.get_object(pet_id, request.user.id)
#         if not Pet_instance:
#             return Response(
#                 {"res": "Object with Pet id does not exists"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         serializer = PetsSerializer(Pet_instance)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def get_object(self, pet_id, user_id):
#         '''
#         Helper method to get the object with given Pet_id, and user_id
#         '''
#         try:
#             return Pets.objects.get(id=pet_id)
#         except Pets.DoesNotExist:
#             return None
        
#     # 4. Update
#     def put(self, request, pet_id, *args, **kwargs):
#         '''
#         Updates the Pet item with given pet_id if exists
#         '''
#         Pet_instance = self.get_object(pet_id, request.user.id)
#         if not Pet_instance:
#             return Response(
#                 {"res": "Object with Pet id does not exists"}, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         data = {
#             'nom': request.data.get('task'), 
#             'completed': request.data.get('completed'), 
#             'user': request.user.id
#         }
#         serializer = PetsSerializer(instance = Pet_instance, data=data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # 5. Delete
#     def delete(self, request, pet_id, *args, **kwargs):
#         '''
#         Deletes the Pet item with given pet_id if exists
#         '''
#         Pet_instance = self.get_object(pet_id, request.user.id)
#         if not Pet_instance:
#             return Response(c
#                 {"res": "Object with Pet id does not exists"}, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         Pet_instance.delete()
#         return Response(
#             {"res": "Object deleted!"},
#             status=status.HTTP_200_OK
#         )

class LoginView(APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data, context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)


class LogoutView(APIView):

    def post(self, request, format=None):
        logout(request)
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user