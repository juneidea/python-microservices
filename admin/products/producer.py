import pika, json

params = pika.URLParameters('amqps://hpawqxju:dlNvPjNvDDNErVi2bns1Anu9YOa_bxjZ@shrimp.rmq.cloudamqp.com/hpawqxju')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)