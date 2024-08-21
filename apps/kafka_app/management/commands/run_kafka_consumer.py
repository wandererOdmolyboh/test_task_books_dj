from django.core.management.base import BaseCommand
from apps.kafka_app.kafka_consumer import consume_messages


class Command(BaseCommand):
    help = 'Run Kafka consumer'

    def handle(self, *args, **options):
        consume_messages()
