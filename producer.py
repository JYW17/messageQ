import pika
import time

# RabbitMQ에 연결 (localhost는 RabbitMQ 서버 주소)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 큐 생성 (존재하지 않으면 생성됨)
channel.queue_declare(queue='iot_queue')

for i in range(10):
    message = f"Message {i+1}"
    channel.basic_publish(exchange='', routing_key='iot_queue', body=message)
    print(f" [x] Sent '{message}'")
    time.sleep(1)  # 1초 대기 (메시지 전송 속도 조절)

connection.close()
