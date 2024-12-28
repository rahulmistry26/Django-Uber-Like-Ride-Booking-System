        
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ride ,User,Role
from .serializers import RideSerializer ,UserSerializer,RoleSerializer
from .middleware import CustomAPIMiddleware
import jwt


class RideView(APIView):
    def get(self, request):
        user = CustomAPIMiddleware.isUserAuth(self, request, [1,2,3])
        if user == False:
           return Response({"message": "Not Authorized to view"}, status=403)
        ride = Ride.objects.all()
        serializer = RideSerializer(ride, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = CustomAPIMiddleware.isUserAuth(self, request, [2])
        if user == False:
          return Response({"message": "Not Authorized to view"}, status=403)
        serializer = RideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RideById(APIView):
    def get_object(self, id):
        try:
            return Ride.objects.get(id=id)
        except Ride.DoesNotExist:
            return None

    def get(self, request, id):
        user = CustomAPIMiddleware.isUserAuth(self, request, [1,2,3])
        if user == False:
             return Response({"message": "Not Authorized to view"}, status=403)
        ride = self.get_object(id)
        if ride is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = RideSerializer(ride)
        return Response(serializer.data)


class RideUpdate(APIView):

    def get_object(self, id):
        try:
            return Ride.objects.get(id=id)
        except Ride.DoesNotExist:
            return None
        
    def put(self, request, id):
        user = CustomAPIMiddleware.isUserAuth(self, request, [3])
        if user == False:
           return Response({"message": "Not Authorized to view"}, status=403)
        ride = self.get_object(id)
        if ride is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = RideSerializer(ride, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        user = self.get_object(pk)
        if user is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class RoleView(APIView):
    def get(self, request):
        role = Role.objects.all()
        serializer = RoleSerializer(role, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserView(APIView):
    def get(self, request):
        user=CustomAPIMiddleware.isUserAuth(self,request,[1,2])
        if not user:
            return Response({"message":"not authorize"})
        print(user,"user")
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


secret="rahul"
class UserLogin(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = User.objects.get(email=email, password=password)
        serializer = UserSerializer(user)
        encoded_jwt = jwt.encode(serializer.data, secret, algorithm="HS256")
        print(encoded_jwt)
        return Response({"token": encoded_jwt, "data": serializer.data})


class UserUpdate(APIView):

    def get_object(self, id=None):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    def get(self, request, id=None):
        user = self.get_object(id)
        if user is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, id=None):
        user = self.get_object(id)
        if user is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)