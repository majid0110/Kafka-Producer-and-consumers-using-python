from kafka import KafkaProducer
from time import sleep
from json import dumps
from CSV import datafromfile



producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])
testdata = datafromfile()
for e in range(3):
    data = {'Count': e}
    producer.send('test', value=data)
    print(data)
    sleep(5)
producer.send('test', value=testdata)
print(testdata)
