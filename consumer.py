import pika

# RabbitMQ에 연결
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 큐 생성 (프로듀서와 같은 이름의 큐)
channel.queue_declare(queue='iot_queue')

# 메시지를 수신할 때 실행할 함수
def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

# iot_queue 큐에서 메시지 수신 대기
channel.basic_consume(queue='iot_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
