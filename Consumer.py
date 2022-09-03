import json
from kafka import KafkaConsumer
from json import loads


if __name__ == '__main__':
    KafkaConsumer = KafkaConsumer(
        'Your_topic_name',
        bootstrap_servers=['127.0.0.1:9092'],
        auto_offset_reset='latest',
        api_version =(0, 10),
        enable_auto_commit=True,
        group_id='consumer-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')))
print('proceeding into for loop')

for massage in KafkaConsumer:
    print(massage)

