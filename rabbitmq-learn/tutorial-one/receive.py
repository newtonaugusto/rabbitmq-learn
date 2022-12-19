import os
import sys

import pika


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1"))
    channel = connection.channel()

    channel.queue_declare(queue="hello")

    channel.basic_consume(queue="hello", auto_ack=True, on_message_callback=callback)
    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
