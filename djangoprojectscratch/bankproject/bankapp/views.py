# from django.shortcuts import render
# from rest_framework.views import APIView
# from . models import *
# from . serializer import *
# from rest_framework.response import Response
# # Create your views here.
 
# class BasicInformationView(APIView):
#     def get(self, request):
#         # Fetch all BasicInformation objects
#         basic_info_objects = BasicInformation.objects.all()
#         # Format the response
#         response_data = [{
#             "id": info.id,
#             "full_name": info.full_name,
#             "father_or_husband_name": info.father_or_husband_name,
#             "gender": info.gender,
#             "occupation": info.occupation,
#             "income": info.income,
#             "kyc_document_number": info.kyc_document_number,
#             "email": info.email,
#             "mobile": info.mobile,
#             "permanent_address": info.permanent_address,
#             "address_details": info.address_details,
#             "communication_address": info.communication_address,
#             "pin_code": info.pin_code
#         } for info in basic_info_objects]
#         return Response(response_data)

#     def post(self, request):
#         serializer = BasicInformationSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
        

# class BasicInfoAccountView(APIView):
#     def get(self, request):
#         # Fetch all BasicInfoAccount objects
#         account_objects = BasicInfoAccount.objects.all()
#         # Format the response
#         response_data = [{
#             "account_number": account.account_number,
#             "loan_amount": account.loan_amount,
#             "loan_requested_for": account.loan_requested_for
#         } for account in account_objects]
#         return Response(response_data)

#     def post(self, request):
#         serializer = BasicInfoAccountSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
        

# class UserView(APIView):
#     def get(self, request):
#         # Fetch all User objects
#         user_objects = User.objects.all()
#         # Format the response
#         response_data = [{
#             "id": user.id,
#             "email": user.email,
#             "role": user.role
#         } for user in user_objects]
#         return Response(response_data)

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)


# class AdminView(APIView):
#     def get(self, request):
#         # Fetch all Admin objects
#         admin_objects = Admin.objects.all()
#         # Format the response
#         response_data = [{
#             "id": admin.id,
#             "email": admin.email,
#             "role": admin.role
#         } for admin in admin_objects]
#         return Response(response_data)

#     def post(self, request):
#         serializer = AdminSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
# //////////////////////////////        


# ////////////////////////////   
# from rest_framework.views import APIView
# from .models import BasicInformation, BasicInfoAccount, User, Admin
# from .serializer import BasicInformationSerializer, BasicInfoAccountSerializer, UserSerializer, AdminSerializer
# from rest_framework.response import Response
# from rest_framework import status

# class BasicInformationView(APIView):
#     def get(self, request):
#         basic_info_objects = BasicInformation.objects.all()
#         response_data = [{
#             "id": info.id,
#             "full_name": info.full_name,
#             "father_or_husband_name": info.father_or_husband_name,
#             "gender": info.gender,
#             "occupation": info.occupation,
#             "income": info.income,
#             "kyc_document_number": info.kyc_document_number,
#             "email": info.email,
#             "mobile": info.mobile,
#             "permanent_address": info.permanent_address,
#             "address_details": info.address_details,
#             "communication_address": info.communication_address,
#             "pin_code": info.pin_code
#         } for info in basic_info_objects]
#         return Response(response_data)

#     def post(self, request):
#         serializer = BasicInformationSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BasicInfoAccountView(APIView):
#     def get(self, request):
#         account_objects = BasicInfoAccount.objects.all()
#         response_data = [{
#             "account_number": account.account_number,
#             "loan_amount": account.loan_amount,
#             "loan_requested_for": account.loan_requested_for
#         } for account in account_objects]
#         return Response(response_data)

#     def post(self, request):
#         serializer = BasicInfoAccountSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserView(APIView):
#     def get(self, request):
#         user_objects = User.objects.all()
#         response_data = [{
#             "id": user.id,
#             "email": user.email,
#             "role": user.role
#         } for user in user_objects]
#         return Response(response_data)

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class AdminView(APIView):
#     def get(self, request):
#         admin_objects = Admin.objects.all()
#         response_data = [{
#             "id": admin.id,
#             "email": admin.email,
#             "role": admin.role
#         } for admin in admin_objects]
#         return Response(response_data)

#     def post(self, request):
#         serializer = AdminSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BasicInformation, BasicInfoAccount, User, Admin
from .serializer import BasicInformationSerializer, BasicInfoAccountSerializer, UserSerializer, AdminSerializer

class BasicInformationView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                info = BasicInformation.objects.get(pk=pk)
                serializer = BasicInformationSerializer(info)
                return Response(serializer.data)
            except BasicInformation.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            basic_info_objects = BasicInformation.objects.all()
            serializer = BasicInformationSerializer(basic_info_objects, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = BasicInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            info = BasicInformation.objects.get(pk=pk)
        except BasicInformation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BasicInformationSerializer(info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            info = BasicInformation.objects.get(pk=pk)
        except BasicInformation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BasicInfoAccountView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                account = BasicInfoAccount.objects.get(pk=pk)
                serializer = BasicInfoAccountSerializer(account)
                return Response(serializer.data)
            except BasicInfoAccount.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            account_objects = BasicInfoAccount.objects.all()
            serializer = BasicInfoAccountSerializer(account_objects, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = BasicInfoAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            account = BasicInfoAccount.objects.get(pk=pk)
        except BasicInfoAccount.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BasicInfoAccountSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            account = BasicInfoAccount.objects.get(pk=pk)
        except BasicInfoAccount.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                user = User.objects.get(pk=pk)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            user_objects = User.objects.all()
            serializer = UserSerializer(user_objects, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AdminView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                admin = Admin.objects.get(pk=pk)
                serializer = AdminSerializer(admin)
                return Response(serializer.data)
            except Admin.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            admin_objects = Admin.objects.all()
            serializer = AdminSerializer(admin_objects, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            admin = Admin.objects.get(pk=pk)
        except Admin.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = AdminSerializer(admin, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            admin = Admin.objects.get(pk=pk)
        except Admin.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        admin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

       
        
        
'''    
#     def get(self, request):
#         output = [{
#             "id": output.id,
#             "full_name": output.full_name,
#             "father_or_husband_name": output.father_or_husband_name,
#             "gender": output.gender,
#             "occupation": output.occupation,
#             "income": output.income,
#             "kyc_document_number": output.kyc_document_number,
#             "email": output.email,
#             "mobile": output.mobile,
#             "permanent_address": output.permanent_address,
#             "address_details": output.address_details,
#             "communication_address": output.communication_address,
#             "pin_code": output.pin_code
#         } for output in BasicInformation.objects.all()]
#         return Response(output)

#     def post(self, request):
#         serializer = BasicInformationSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
        

# class BasicInfoAccountView(APIView):
#     def get(self, request):
#         output = [{
#             "account_number": output.account_number,
#             "loan_amount": output.loan_amount,
#             "loan_requested_for": output.loan_requested_for
#         } for output in BasicInfoAccount.objects.all()]
#         return Response(output)

#     def post(self, request):
#         serializer = BasicInfoAccountSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
        

# class UserView(APIView):
#     def get(self, request):
#         output = [{
#             "id": output.id,
#             "email": output.email,
#             "role": output.role
#         } for output in User.objects.all()]
#         return Response(output)

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
        

# class AdminView(APIView):
#     def get(self, request):
#         output = [{
#             "id": output.id,
#             "email": output.email,
#             "role": output.role
#         } for output in Admin.objects.all()]
#         return Response(output)

#     def post(self, request):
#         serializer = AdminSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

'''