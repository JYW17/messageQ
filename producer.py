import pika
import time
import argparse  # 명령줄 인자를 파싱하기 위한 모듈

# 명령줄 인자 파서 설정
parser = argparse.ArgumentParser(description='IoT device message producer')
parser.add_argument('device_number', type=int, 
                    help='Device number (1-99)',
                    choices=range(1, 100))  # 1부터 99까지만 허용

args = parser.parse_args()

# IoT 장비 이름 생성 (예: iot_no_01, iot_no_02, ...)
device_name = f'iot_no_{args.device_number:02d}'  # :02d는 2자리 숫자로 포맷팅

# RabbitMQ에 연결
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='127.0.0.1',
        port=5672,
        credentials=pika.PlainCredentials('guest', 'guest'),
        heartbeat=600,
        blocked_connection_timeout=300
    )
)
channel = connection.channel()

# 큐 생성
channel.queue_declare(queue='iot_queue')

for i in range(10):
    sensor_data = f"Sensor data {i+1}"
    message = f"{device_name} - {sensor_data}"
    channel.basic_publish(exchange='', routing_key='iot_queue', body=message)
    print(f" [x] Sent '{message}'")
    time.sleep(1)

connection.close()
