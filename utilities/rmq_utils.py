import os
import pika
import json
import time
from dotenv import load_dotenv
from pika.exceptions import AMQPConnectionError

from utilities.logging_config import get_logger

load_dotenv()
logger = get_logger(__name__)


def create_connection(retries=5, delay=2):
    breakpoint()
    credentials = pika.PlainCredentials(
        os.getenv("RABBITMQ_USER", "guest"),
        os.getenv("RABBITMQ_PASS", "guest")
    )
    host = os.getenv("RABBITMQ_HOST", "127.0.0.1")
    port = int(os.getenv("RABBITMQ_PORT", 5672))

    for attempt in range(1, retries + 1):
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=host, port=port, credentials=credentials)
            )
            print(f"Connected to RabbitMQ on attempt {attempt}")
            return connection
        except (AMQPConnectionError, OSError) as e:
            print(f"Attempt {attempt} failed: {e}")
            time.sleep(delay)
    
    raise ConnectionError(f"Could not connect to RabbitMQ at {host}:{port} after {retries} attempts")



def publish_to_rabbimq(queue, payload):
    """Safely publish a message to RabbitMQ."""
    try:
        connection = create_connection()
        channel = connection.channel()
        channel.queue_declare(queue=queue, durable=True)

        if not isinstance(payload, (str, bytes)):
            payload = json.dumps(payload)

        channel.basic_publish(
            exchange='',
            routing_key=queue,
            body=payload,
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )
        logger.info(f"Message published to queue: {queue}")
    except Exception as e:
        logger.exception(f"RabbitMQ publish failed: {e}")
    finally:
        try:
            connection.close()
        except Exception:
            pass

