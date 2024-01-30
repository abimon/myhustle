from django.http import JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

@csrf_exempt
def register(request):
    return render(request,'auth/register.html')
def signin(request):
    return render(request,'auth/login.html')
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        avatar = request.FILES.get('avatar')
        instance = User(name=name,email=email,contact=contact,password=make_password(password),avatar=avatar)
        instance.save()
        person = {
            'id':instance.id,
            'name':instance.name,
            'email':instance.email,
            'contact':instance.contact,
            'avatar':instance.avatar.url
        }
        return JsonResponse(person)
    else:
        return JsonResponse({'error': 'An error occurred'}, status=400)
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            passwordB = user.password
            if check_password(password, passwordB):
                data = {
                    'id':user.id,
                    'name':user.name,
                    'email':user.email,
                    'contact':user.contact,
                    'avatar':user.avatar.url
                }
                return JsonResponse(data)
            else:
                return JsonResponse({"error":"Wrong password"})
        except User.DoesNotExist:
            return JsonResponse({"error":"No user found with that email."})