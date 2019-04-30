from django.conf.urls import url
from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'


urlpatterns = [
    path('', mainapp.media, name='media'),
    path('<int:pk>/', mainapp.media, name='category'),

]

