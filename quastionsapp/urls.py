from django.urls import path

import quastionsapp.views as quastionsapp

app_name = 'quastionsapp'

urlpatterns = [
    path('', quastionsapp.questions, name='questions'),
    path('send_email/', quastionsapp.send_email, name='send_email'),
]
