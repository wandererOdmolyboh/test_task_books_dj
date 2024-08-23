from confluent_kafka import Consumer, KafkaException, KafkaError

kafka_conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'django-consumer-group',
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(kafka_conf)
consumer.subscribe(['books_topic'])


def consume_messages():
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                raise KafkaException(msg.error())
        print(f"Consumed message: {msg.value().decode('utf-8')}")
