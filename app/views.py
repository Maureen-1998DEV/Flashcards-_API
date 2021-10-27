from django.shortcuts import render

from app.permissions import IsAdminOrReadOnly
from .models import Profile, Course, Note
from django.contrib.auth.models import User

# authentication
from django.contrib.auth import authenticate, login, logout


# api
from django.http import JsonResponse
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import CourseSerializer, NoteSerializer, ProfileSerializer, UserSerializer,UserCreateSerializer
from .permissions import IsAdminOrReadOnly


# Create your views here.

def index(request):
    return render(request, 'index.html')




class UserList(APIView): 
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserCreate(APIView): 
    permission_classes = (IsAdminOrReadOnly,)

    def post(self, request, format=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class loginUser(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class logoutUser(APIView): 
    def get(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class SubjectList(APIView):  
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):  
        all_Subjects = Course.objects.all()
        serializers = CourseSerializer(all_Subjects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):  
        serializers = CourseSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class SubjectDetail(APIView):  
    permission_classes = (IsAdminOrReadOnly,)

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):  
        subject = self.get_object(pk)
        serializers = CourseSerializer(subject)
        return Response(serializers.data)

    def put(self, request, pk, format=None):  
        subject = self.get_object(pk)
        serializers = CourseSerializer(subject, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):  
        subject = self.get_object(pk)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NotesList(APIView):  
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):  
        all_notes = Note.objects.all()
        serializers = NoteSerializer(all_notes, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):  # create new note
        serializers = NoteSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class NotesDetail(APIView):  
    permission_classes = (IsAdminOrReadOnly,)

    def get_object(self, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):  # get note
        notes = self.get_object(pk)
        serializers = NoteSerializer(notes)
        return Response(serializers.data)

    def put(self, request, pk, format=None):  # update note
        notes = self.get_object(pk)
        serializers = NoteSerializer(notes, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):  # delete note
        notes = self.get_object(pk)
        notes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ProfileList
class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# ProfileDetail
class ProfileDetail(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializers = ProfileSerializer(profile, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
