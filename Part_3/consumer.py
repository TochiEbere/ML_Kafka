from utils import parse_args
from event_stream import KafkaStream, GooglePubsub
import sys


args = parse_args()
BROKER_TYPE = args.broker_type
TOPIC = args.topic_name
GCP_CREDS = args.gcp_credentials
SUB_ID = args.subscription_id
PROJECT_ID = args.project_id
broker_type = BROKER_TYPE

def consumer(broker_type, topic, gcp_creds=None, sub_id=None, project_id=None):

    if broker_type=='kafka':
        kafka_broker = KafkaStream(topic)
        image = kafka_broker.consume()
        return image

    else:
        pub_sub = GooglePubsub(topic, gcp_creds)
        result = pub_sub.consume(sub_id, project_id)
        return result

# try:
#     result = consumer(broker_type=BROKER_TYPE)
# except KeyboardInterrupt:
#     pass

consumer(broker_type=BROKER_TYPE, topic='inference')