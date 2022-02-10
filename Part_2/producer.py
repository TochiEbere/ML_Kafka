from utils import parse_args
from event_stream import KafkaStream, GooglePubsub

args = parse_args()

BROKER_TYPE = args.broker_type
TOPIC = args.topic_name
IMAGE = args.image_path
GCP_CREDS = args.gcp_credentials
SUB_ID = args.subscription_id
PROJECT_ID = args.project_id


def producer(broker_type, topic, image, gcp_creds=None, project_id=None):
    if broker_type=='kafka':
        kafka_broker = KafkaStream(topic)
        data = kafka_broker.data_encoder(image)
        kafka_broker.produce()
    else:
        pub_sub = GooglePubsub(topic, gcp_creds)
        pub_sub.produce(project_id)


producer(broker_type=BROKER_TYPE, topic=TOPIC, image=IMAGE)
