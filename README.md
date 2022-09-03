# Kafka Producer and consumers using python
This will show you how to send data by producer and capture by consumer using python

# CSV.py
In first step we will need to upload data to 'CSV.py' file. It will read data from CSV and it will be used for Producer. Shown as
![image](https://user-images.githubusercontent.com/81530072/188285696-4658810a-74b5-4d5e-8eb3-402880df4d6e.png)




# Producer.py
Before heading to Producer, you will need to create a topic using below command (in Windows)
kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
Now we will use Prodecer for sending data from CSV into Consumer in real time. For this you will need to make sure your Zookeeper and Kafka running at the same time. As Shown in the figure:
# Zookeeper Server:
![image](https://user-images.githubusercontent.com/81530072/188285961-c829480a-544a-4d32-b4ae-532b16b4d29f.png)


# Kafka Server:
![image](https://user-images.githubusercontent.com/81530072/188285946-d20c6597-2612-4f93-ad36-d05decdbdfcb.png)

After starting these two, Now you will need to run Producer.py and it will send data to Concumer.

# Consumer
It's all set for consumer to catch the data from producer , you just need to run  consumer code...


