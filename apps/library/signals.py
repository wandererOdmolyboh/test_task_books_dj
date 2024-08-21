from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book
from apps.kafka_app.kafka_producer import send_message


@receiver(post_save, sender=Book)
def book_post_save(sender, instance, **kwargs):
    message = f"New book added: {instance.title} by {instance.author}"
    send_message('books_topic', message)
