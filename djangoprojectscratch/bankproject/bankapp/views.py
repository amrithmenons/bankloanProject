
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import *
# from .serializer import *

# class UserView(APIView):
#     def get(self, request, pk=None):
#         if pk:
#             try:
#                 user = User.objects.get(pk=pk)
#                 serializer = UserSerializer(user)
#                 return Response(serializer.data)
#             except User.DoesNotExist:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#         else:
#             user_objects = User.objects.all()
#             serializer = UserSerializer(user_objects, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk=None):
#         try:
#             user = User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         serializer = UserSerializer(user, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk=None):
#         try:
#             user = User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         try:
#             user = User.objects.get(email=email)
#             if user.check_password(password):
#                 return Response({"detail": "User authenticated successfully."}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"detail": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)
#         except User.DoesNotExist:
#             return Response({"detail": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)


# class AdminView(APIView):
#     def get(self, request, pk=None):
#         if pk:
#             try:
#                 admin = Admin.objects.get(pk=pk)
#                 serializer = AdminSerializer(admin)
#                 return Response(serializer.data)
#             except Admin.DoesNotExist:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#         else:
#             admin_objects = Admin.objects.all()
#             serializer = AdminSerializer(admin_objects, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#         serializer = AdminSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk=None):
#         try:
#             admin = Admin.objects.get(pk=pk)
#         except Admin.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         serializer = AdminSerializer(admin, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk=None):
#         try:
#             admin = Admin.objects.get(pk=pk)
#         except Admin.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         admin.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

        
        
# class BasicInformationView(APIView):
#     def get(self, request, pk=None):
#         if pk:
#             try:
#                 info = BasicInformation.objects.get(pk=pk)
#                 serializer = BasicInformationSerializer(info)
#                 return Response(serializer.data)
#             except BasicInformation.DoesNotExist:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#         else:
#             basic_info_objects = BasicInformation.objects.all()
#             serializer = BasicInformationSerializer(basic_info_objects, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#         serializer = BasicInformationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk=None):
#         try:
#             info = BasicInformation.objects.get(pk=pk)
#         except BasicInformation.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         serializer = BasicInformationSerializer(info, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk=None):
#         try:
#             info = BasicInformation.objects.get(pk=pk)
#         except BasicInformation.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         info.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# class BasicInfoAccountView(APIView):
#     def get(self, request, pk=None):
#         if pk:
#             try:
#                 account = BasicInfoAccount.objects.get(pk=pk)
#                 serializer = BasicInfoAccountSerializer(account)
#                 return Response(serializer.data)
#             except BasicInfoAccount.DoesNotExist:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#         else:
#             account_objects = BasicInfoAccount.objects.all()
#             serializer = BasicInfoAccountSerializer(account_objects, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#         account_number = request.data.get('account_number')

#         # Check if the account number exists in BasicInformation
#         try:
#             basic_info = BasicInformation.objects.get(id=account_number)
#         except BasicInformation.DoesNotExist:
#             return Response(
#                 {"detail": "Account number does not exist. Please create an account first."},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         # If account number exists, proceed with creating the BasicInfoAccount
#         serializer = BasicInfoAccountSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk=None):
#         try:
#             account = BasicInfoAccount.objects.get(pk=pk)
#         except BasicInfoAccount.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         serializer = BasicInfoAccountSerializer(account, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk=None):
#         try:
#             account = BasicInfoAccount.objects.get(pk=pk)
#         except BasicInfoAccount.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         account.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
'''
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BasicInformation, BasicInfoAccount, User, Admin
from .serializer import BasicInformationSerializer, BasicInfoAccountSerializer, UserSerializer, AdminSerializer

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
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
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
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


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
            admins = Admin.objects.all()
            serializer = AdminSerializer(admins, many=True)
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
            serializer = AdminSerializer(admin, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Admin.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        try:
            admin = Admin.objects.get(pk=pk)
            admin.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Admin.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
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
            infos = BasicInformation.objects.all()
            serializer = BasicInformationSerializer(infos, many=True)
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
            serializer = BasicInformationSerializer(info, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except BasicInformation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        try:
            info = BasicInformation.objects.get(pk=pk)
            info.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except BasicInformation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

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
            accounts = BasicInfoAccount.objects.all()
            serializer = BasicInfoAccountSerializer(accounts, many=True)
            return Response(serializer.data)

    def post(self, request):
        account_number = request.data.get('account_number')
        try:
            BasicInformation.objects.get(id=account_number)
        except BasicInformation.DoesNotExist:
            return Response(
                {"detail": "Account number does not exist. Please create an account first."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = BasicInfoAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            account = BasicInfoAccount.objects.get(pk=pk)
            serializer = BasicInfoAccountSerializer(account, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except BasicInfoAccount.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        try:
            account = BasicInfoAccount.objects.get(pk=pk)
            account.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except BasicInfoAccount.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
'''
   

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BasicInformation, BasicInfoAccount, User, Admin
from .serializer import BasicInformationSerializer, BasicInfoAccountSerializer, UserSerializer, AdminSerializer
from django.contrib.auth import authenticate
from django.http import JsonResponse
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
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

   
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    from django.contrib.auth import authenticate
    def post_login(self, request):
        """
        Handle login requests.
        """
        if request.method == 'POST':
            email = request.data.get('email')
            password = request.data.get('password')
            
            user = authenticate(request, username=email, password=password)
            if user is not None:
                return Response({'success': True, 'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def put(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


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
            admins = Admin.objects.all()
            serializer = AdminSerializer(admins, many=True)
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
            serializer = AdminSerializer(admin, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Admin.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        try:
            admin = Admin.objects.get(pk=pk)
            admin.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Admin.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
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
            infos = BasicInformation.objects.all()
            serializer = BasicInformationSerializer(infos, many=True)
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
            serializer = BasicInformationSerializer(info, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except BasicInformation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        try:
            info = BasicInformation.objects.get(pk=pk)
            info.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except BasicInformation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

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
            accounts = BasicInfoAccount.objects.all()
            serializer = BasicInfoAccountSerializer(accounts, many=True)
            return Response(serializer.data)

    def post(self, request):
        account_number = request.data.get('account_number')
        try:
            BasicInformation.objects.get(id=account_number)
        except BasicInformation.DoesNotExist:
            return Response(
                {"detail": "Account number does not exist. Please create an account first."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = BasicInfoAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            account = BasicInfoAccount.objects.get(pk=pk)
            serializer = BasicInfoAccountSerializer(account, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except BasicInfoAccount.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        try:
            account = BasicInfoAccount.objects.get(pk=pk)
            account.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except BasicInfoAccount.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
