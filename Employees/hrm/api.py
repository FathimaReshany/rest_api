

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from .serializers import *

from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.authtoken.models import Token


class UserAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer =self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token.created=Token.objects.get_or_create(user=user)
        return Response(Token.key)

class UserList(APIView):
    def get(self, request):

        model = Users.objects.all()
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data)



    def post(self,request):

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get(self, request, emp_id):
        try:
            model = Users.objects.get(id=emp_id)
        except Users.DoesNotExist:
            return Response(f'User With Employee ID {emp_id} Is Not Found' ,status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(model)
        return Response(serializer.data)



    def put(self,request,emp_id):

        try:
            model = Users.objects.get(id=emp_id)
        except Users.DoesNotExist:
            return Response(f'User With Employee ID {emp_id} Is Not Found' ,status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




    def delete(self,request,emp_id):

        try:
            model = Users.objects.get(id=emp_id)
        except Users.DoesNotExist:
            return Response(f'User With Employee ID {emp_id} Is Not Found' ,status=status.HTTP_404_NOT_FOUND)

        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







