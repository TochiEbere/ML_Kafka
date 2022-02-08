from utils import parse_broker_args
from event_stream import KafkaStream, GooglePubsub

args = parse_broker_args()

BROKER_TYPE = args.broker_type
TOPIC = args.topic_name
IMAGE = args.image_path
GCP_CREDS = args.gcp_credentials
SUB_ID = args.subscription_id
PROJECT_ID = args.project_id


def main(broker_type):
    if broker_type=='kafka':
        kafka_broker = KafkaStream(TOPIC)
        data = kafka_broker.data_encoder(IMAGE)
        image = kafka_broker.consume()
        kafka_broker.produce()
        return image

    else:
        pub_sub = GooglePubsub(TOPIC, GCP_CREDS)
        result = pub_sub.consume(SUB_ID, PROJECT_ID)
        pub_sub.produce(PROJECT_ID)
        return result


if __name__== '__main__':
    main(broker_type=BROKER_TYPE)

