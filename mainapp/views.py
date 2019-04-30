from django.shortcuts import render
from .models import Event, EventCategory, Document
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def main(request):
    title = 'главная'

    events = Event.objects.filter(is_active=True, category__is_active=True)[:3]

    content = {
        'title': title,
        'events': events,
    }
    return render(request, 'mainapp/index.html', content)

def about(request):
    title = 'О нас | Стюарды.рф'

    content = {'title': title}

    return render(request, 'mainapp/about.html', content)

# def anketa(request):
#     title = 'Анкета | Стюарды.рф'
#
#     content = {'title': title}
#     return render(request, 'mainapp/anketa.html', content)

def contacts(request):
    title = 'Контакты | Стюарды.рф'

    content = {'title': title}
    return render(request, 'mainapp/contacts.html', content)

def documents(request):
    title = 'Документы | Стюарды.рф'

    documents = Document.objects.all()

    content = {
        'title': title,
        'documents': documents,
    }
    return render(request, 'mainapp/documents.html', content)

def faq(request):
    title = 'FAQ | Стюарды.рф'

    content = {'title': title}
    return render(request, 'mainapp/faq.html', content)

def media(request):
    title = 'Медиа | Стюарды.рф'

    events = Event.objects.filter(is_active=True, category__is_active=True)

    content = {'title': title,
               'events': events,
               }

    return render(request, 'mainapp/media.html', content)

def vacancy(request):
    title = 'Вакансии | Стюарды.рф'

    content = {'title': title}
    return render(request, 'mainapp/vacancy.html', content)

