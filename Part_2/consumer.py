from utils import parse_broker_args
from event_stream import KafkaStream, GooglePubsub


def consumer(broker_type):

    args = parse_broker_args()
    global BROKER_TYPE
    BROKER_TYPE = args.broker_type
    TOPIC = args.topic_name
    GCP_CREDS = args.gcp_credentials
    SUB_ID = args.subscription_id
    PROJECT_ID = args.project_id
    broker_type = BROKER_TYPE

    if broker_type=='kafka':
        kafka_broker = KafkaStream(TOPIC)
        image = kafka_broker.consume()
        return image

    else:
        pub_sub = GooglePubsub(TOPIC, GCP_CREDS)
        result = pub_sub.consume(SUB_ID, PROJECT_ID)
        return result

result = consumer(broker_type=BROKER_TYPE)
print(result)