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

    producer.poll(0)

    producer.produce(topic, message, callback=delivery_report)

    # Wait for any outstanding messages to be delivered and delivery reports to be triggered
    producer.flush()
