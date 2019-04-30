from django.core.management.base import BaseCommand
from mainapp.models import Event, EventCategory, Document
from django.contrib.auth.models import User

import json, os

JSON_PATH = 'mainapp/json'


def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = loadFromJSON('categories')

        EventCategory.objects.all().delete()
        for category in categories:
            new_category = EventCategory(**category)
            new_category.save()

        events = loadFromJSON('events')

        Event.objects.all().delete()
        for event in events:
            category_name = event["category"]
            # Получаем категорию по имени
            _category = EventCategory.objects.get(name=category_name)
            # Заменяем название категории объектом
            event['category'] = _category
            new_event = Event(**event)
            new_event.save()

        documents = loadFromJSON('documents')

        Document.objects.all().delete()
        for document in documents:
            new_document = Document(**document)
            new_document.save()
