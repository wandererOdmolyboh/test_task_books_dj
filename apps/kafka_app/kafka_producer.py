from confluent_kafka import Producer

kafka_conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'django-producer',
}

producer = Producer(kafka_conf)


def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')


def send_message(topic, message):
    producer.produce(topic, message.encode('utf-8'), callback=delivery_report)
    producer.flush()
