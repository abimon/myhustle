from django.urls import path
from .views import FileUploadViewSet,items,show
urlpatterns=[
    path('upload/',FileUploadViewSet.as_view(),name='uploadFile'),
    path('view/',items,name='view'),
    path('show/<id>',show,name='show'),
]