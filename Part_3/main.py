from utils import parse_args
import json
from tensorflow.keras.models import load_model
import tensorflow_datasets as tfds
import numpy as np
from Part_2 import consumer

def main():

    args = parse_args()

    MODEL_PATH = args.model_path
    LABEL_PATH = args.label_path
    DATA_SOURCE = args.data_source
    IMAGE_PATH = args.image_path
    TARGET_SIZE = args.target_size

    model = load_model('model.h5', compile = True)

    img = consumer.consumer()


    if DATA_SOURCE == 'fashion_mnist':
        class_labels = tfds.builder("fashion_mnist").info.features["label"]
        pred = model.predict(img)
        prediction = np.argmax(pred)
        label = class_labels.int2str(prediction)
    else:
        with open(LABEL_PATH) as json_file:
            class_labels = json.load(json_file)

        pred = model.predict(img)
        prediction = np.argmax(pred)
        label = class_labels[prediction]
    
    return label