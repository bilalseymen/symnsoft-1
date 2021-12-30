from django.urls import path
from symnsoft.views import index, singlepage

urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug>', singlepage, name='singlepage'),
]
