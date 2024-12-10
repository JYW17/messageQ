import pika

# RabbitMQ에 연결
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='127.0.0.1',
        port=5672,
        credentials=pika.PlainCredentials('guest', 'guest')
    )
)
channel = connection.channel()

# 큐 생성
channel.queue_declare(queue='iot_queue')

# 메시지를 수신할 때 실행할 함수
def callback(ch, method, properties, body):
    import datetime
    message = body.decode()
    device_name, sensor_data = message.split(' - ', 1)
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f" [x] {current_time} - {device_name} - {sensor_data}")

# iot_queue 큐에서 메시지 수신 대기
channel.basic_consume(queue='iot_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
