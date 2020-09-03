from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import SignupSerializer,HealthSerializer
from .models import Signup,Health_Professional_Account
from django.views.decorators.csrf import csrf_exempt

# REST Framework api_view() Decorator  Start
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# REST Framework api_view() Decorator  End



# class based api views start
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# class SignupView(APIView):
#      # Authentication code
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated]
#     def get(self,request):
#         articles=Signup.objects.all()
#         serializer = SignupSerializer(articles,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer=SignupSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# class LoginView(APIView):
#     def post(self,request):
#         serializer=SignupSerializer
#         Email=request.data.get('Email')
#         Password=request.data.get('Password')
#         authenticate=Signup.objects.filter(Email=Email,Password=Password)
#         if authenticate:
#             return Response(status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)



# class EditView(APIView):
#     def get_object(self,id):
#         try:
#             return Signup.objects.get(id=id)
#         except Signup.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, id):
#         signup = self.get_object(id)
#         serializer = SignupSerializer(signup)
#         return Response(serializer.data)

#     def put(self, request,id):
#         signup = self.get_object(id)
#         serializer = SignupSerializer(signup, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         signup = self.get_object(id)
#         signup.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Doctor Signup
class SignupView(APIView):
    
    def get(self,request):
        health=Health_Professional_Account.objects.all()
        serializer = HealthSerializer(health,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=HealthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            id=serializer.Health_Professional_Account_Id
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
# Doctor Login     
class LoginView(APIView):
    def post(self,request):
        try:
            serializer=HealthSerializer
            Email=request.data.get('Email')
            Password=request.data.get('Password')
            authenticate=Health_Professional_Account.objects.get(Email=Email)
            if authenticate:
                if authenticate.Password == Password:

                    request.session['id']=authenticate.Health_Professional_Account_Id
                    return Response(request.session['id'],status=status.HTTP_201_CREATED)
                else:
                    message={
                    'message':'Password Does Not Match'
                }
                    
                    return Response(message)
        except:
            message={
                'message':'Email Does Not Exist'
            }
            return Response(message)
    

class EditView(APIView):

    def post(self,request):
        try:
            serializer=SignupSerializer
            Email=request.data.get('Email')
            authenticate=Health_Professional_Account.objects.get(Email=Email)
            if authenticate:
                Password=request.data.get('Password')
                authenticate.Password=Password
                authenticate.save()
                message={
                    'message':'Password Updated Successfully'
                }
                return Response(message)
            else:
                message={
                    'message':'Email Does Not Exist'
                }
                return Response(message)
        except:
            message={
                'message':'Email Does Not Exist'
            }
            return Response(message)
   


