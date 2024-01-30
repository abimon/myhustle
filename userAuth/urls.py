from django.urls import path,  include
from . import views
urlpatterns = [
    path('register/', views.register,name='register'),
    path('signin/', views.signin,name='signin'),
    path('create/', views.create,name='create'),
    path('login/', views.login,name='login')

]