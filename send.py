#!/usr/bin/env python
import pika

# Estabelecer conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Garantir que a fila existe
channel.queue_declare(queue='hello')

# Publicar uma mensagem na fila
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

# Mensagem de log informando que a mensagem foi enviada
print(" [x] Sent 'Hello World!'")

# Fechar a conexão
connection.close()
