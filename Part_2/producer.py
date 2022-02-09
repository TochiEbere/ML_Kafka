from utils import parse_broker_args
from event_stream import KafkaStream, GooglePubsub

args = parse_broker_args()

BROKER_TYPE = args.broker_type
TOPIC = args.topic_name
IMAGE = args.image_path
GCP_CREDS = args.gcp_credentials
SUB_ID = args.subscription_id
PROJECT_ID = args.project_id


def producer(broker_type):
    if broker_type=='kafka':
        kafka_broker = KafkaStream(TOPIC)
        data = kafka_broker.data_encoder(IMAGE)
        kafka_broker.produce()
    else:
        pub_sub = GooglePubsub(TOPIC, GCP_CREDS)
        pub_sub.produce(PROJECT_ID)


producer(broker_type=BROKER_TYPE)
