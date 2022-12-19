import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1"))
channel = connection.channel()

channel.queue_declare(queue="hello")

body = "Hello World!"

channel.basic_publish(exchange="", routing_key="hello", body=body)
print(f" [x] Sent '{body}'")

connection.close()
