import json

from django.db.models.signals import post_save
from django.dispatch import receiver

from services.kafka.kafka_producer import send_message
from .models import Book


@receiver(post_save, sender=Book)
def book_post_save(sender, instance, **kwargs):
    message = {
        "title": instance.title,
        "author": {
            "name": instance.owner.username,
            "email": instance.owner.email,  # Assuming the author model has an email field
        }
    }

    send_message('books_topic', json.dumps(message))
