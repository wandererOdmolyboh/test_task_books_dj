import json

from confluent_kafka import Consumer, KafkaError, KafkaException
from django.core.mail import send_mail

from config import settings

kafka_conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'django-consumer-group',
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(kafka_conf)
consumer.subscribe(['books_topic'])


def consume_messages():
    try:
        print("Consuming messages...")
        while True:

            msg = consumer.poll(timeout=1.0)
            print('Message send', msg)
            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    raise KafkaException(msg.error())

            # Декодирование сообщения и загрузка его в словарь
            data = json.loads(msg.value().decode('utf-8'))
            email_subject = 'New Book Created'
            email_body = f'A new book titled "{data["title"]}" has been added to the library.'
            print('Message:', data)
            send_mail(
                email_subject,
                email_body,
                settings.EMAIL_HOST_USER,
                [data["author"]["email"]],  # Assuming the author model has an email field
                fail_silently=False,
            )
            print('Sent email to', data["author"]["email"])
    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        consumer.close()
