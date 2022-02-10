from utils import parse_args
import json
import tensorflow as tf
from tensorflow.keras.models import load_model
import tensorflow_datasets as tfds
import numpy as np
import sys

sys.path.append('C:\\Users\\Best\\Documents\\VectorAI_Assessment')

from Part_2 import consumer


def main(model_path, target_size, data_source, label_path,
        broker_type, topic, gcp_creds=None, sub_id=None, project_id=None):

    model = load_model(model_path, compile = True)

    try:
        img = consumer.consumer(broker_type, topic, gcp_creds=None, sub_id=None, project_id=None)
    except KeyboardInterrupt:
        pass

    img = img.resize((target_size,target_size))
    np_img = np.array(img)
    np_img = tf.cast(np_img, tf.float32) / 255.
    np_img = np.expand_dims(np_img, axis=0)

    if data_source == 'fashion_mnist':
        class_labels = tfds.builder("fashion_mnist").info.features["label"]

        pred = model.predict(np_img)
        prediction = np.argmax(pred)
        label = class_labels.int2str(prediction)
    else:
        with open(label_path) as json_file:
            class_labels = json.load(json_file)

        pred = model.predict(img)
        prediction = np.argmax(pred)
        label = class_labels[prediction]
    
    return label

if __name__ == "__main__":

    args = parse_args()
    BROKER_TYPE = args.broker_type
    TOPIC = args.topic_name
    GCP_CREDS = args.gcp_credentials
    SUB_ID = args.subscription_id
    PROJECT_ID = args.project_id
    MODEL_PATH = args.model
    LABEL_PATH = args.labels
    DATA_SOURCE = args.data_source
    TARGET_SIZE = args.target_size

    prediction = main(
        model_path=MODEL_PATH, 
        target_size=TARGET_SIZE, 
        data_source=DATA_SOURCE, 
        label_path=LABEL_PATH, 
        broker_type=BROKER_TYPE, 
        topic=TOPIC)
    
    print('Your image was predicted as', prediction)