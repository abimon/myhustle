from rest_framework import generics, permissions, status
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import FileUpload
from .serializers import FileUploadSerializer
def show(request,id):
    return JsonResponse(list(FileUpload.objects.filter(user_id=id).values()), safe=False)
def items(request):
    return JsonResponse(list(FileUpload.objects.all().values()), safe=False)

class FileUploadViewSet(generics.CreateAPIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
