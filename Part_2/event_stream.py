import base64
from PIL import Image
from io import BytesIO
from kafka import KafkaProducer, KafkaConsumer
import numpy as np
from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1
import os
# run an arg parser


class StreamRequest():

    def __init__(self, topic_name):
        self.topic = topic_name

    def data_encoder(self, image_path):
        with open(image_path, "rb") as image_file:
            data = base64.b64encode(image_file.read())
        self.encoded_data = data
        return data

class KafkaStream(StreamRequest):

    def __init__(self, topic_name):
        super().__init__(topic_name)

    def consume(self, bootstrap_server=['localhost:9092']):
        consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=bootstrap_server,
            auto_offset_reset='earliest',
            enable_auto_commit=True
            )
        for message in consumer:
            stream = BytesIO(message.value)
            image = Image.open(stream).convert("RGBA")
            stream.close()
        return image

    def produce(self, bootstrap_server=['localhost:9092']):
        producer=KafkaProducer(bootstrap_server)
        producer.send(self.topic, self.encoded_data.tobytes())
    


class GooglePubsub(StreamRequest):

    def __init__(self, topic_name, path_to_credentials):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= path_to_credentials
        super().__init__(topic_name)
    
    def consume(self, subscription_id, project_id):
        subscriber = pubsub_v1.SubscriberClient()
        subscription_path = subscriber.subscription_path(project_id, subscription_id)

        def callback(message: pubsub_v1.subscriber.message.Message) -> None:
            print(f"Received {message}.")
            message.ack()

        streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
        print(f"Listening for messages on {subscription_path}..\n")

        with subscriber:
            try:
                result = streaming_pull_future.result(timeout=15)
            except TimeoutError:
                streaming_pull_future.cancel()  # Trigger the shutdown.
                streaming_pull_future.result()  # Block until the shutdown is complete.
        
        return result

    def produce(self, project_id):
        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(project_id, self.topic)
        future = publisher.publish(topic_path, self.encoded_data)
        print(f"Published messages to {topic_path}.")
