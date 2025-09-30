import pika

# Estabelecer conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Garantir que a fila existe
channel.queue_declare(queue='hello')

# Função de callback para processar mensagens recebidas
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Configurar o consumidor para a fila 'hello'
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

print('> Esperando por mais mensagens.')

# Iniciar o loop de consumo
channel.start_consuming()