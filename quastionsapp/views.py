from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.conf import settings
from quastionsapp.models import UserContact


# Create your views here.
from django.views.generic import DetailView


def questions(request):
    title = 'Анкета'

    content = {'title': title}

    return render(request, 'quastionsapp/anketa.html', content)


class UserContactView(DetailView):
    model = UserContact
    template_name = 'quastionsapp/anketa.html'



def send_email(request):
    subject = 'Anketa'
    full_name = request.POST.get('full_name', '')
    age = request.POST.get('age', '')
    phone_number = request.POST.get('phone_number', '')
    city = request.POST.get('city', '')
    about = request.POST.get('about', '')
    sender = request.POST.get('sender', '')
    message = f'Данные пользователя {full_name} + {age}+ {phone_number} + {city} + {about} + {sender}'

    if subject and message:
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, settings.EMAIL_HOST_USER, fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contants/')
    else:
        return HttpResponse('Убедитесь, что все поля заполнены правильно')

# def send_email(request):
#     subject = 'Anketa'
#     full_name = request.POST['full_name']
#     age = request.POST['age']
#     phone_number = request.POST['phone_number']
#     city = request.POST['city']
#     about = request.POST['about']
#     sender = request.POST['sender']
#     message = full_name + age + phone_number + city + about + sender
#
#     if subject and message:
#         try:
#             send_mail(subject, message, settings.EMAIL_HOST_USER, settings.EMAIL_HOST_USER, fail_silently=False)
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return HttpResponseRedirect('/contants/')
#     else:
#         return HttpResponse('Убедитесь, что все поля заполнены правильно')


