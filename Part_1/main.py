import numpy as np
from CNN_pipeline import CnnPipeline
from utils import parse_cnn_args, data_generator
import tensorflow as tf
import json


def main():

    args = parse_cnn_args()
    MODEL_PATH = args.model_path
    DATA_SOURCE = args.data_source
    TARGET_SIZE = args.target_size
    NUM_CLASSES = args.num_class
    DATA_DIRECTORY = args.data_dir
    TARGET_SIZE = args.target_size
    EPOCH = args.num_epoch
    OPTIMIZER="adam"
    LOSS = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

    train_data, test_data = data_generator(
        source=DATA_SOURCE,
        data_dir=DATA_DIRECTORY,
        target_size=TARGET_SIZE
        )
    
    if DATA_SOURCE !='fashion_mnist':
        labels = train_data.class_indices
        with open("label.json", "w") as outfile:
            json.dump(labels, outfile)

    model_pipeline = CnnPipeline(train_data, test_data)
    model_pipeline.model_architecture(TARGET_SIZE, NUM_CLASSES, OPTIMIZER, LOSS)
    cnn_model = model_pipeline.train_CNNmodel(num_epoch=EPOCH)
    model_pipeline.model_accuracy()
    cnn_model.save("{}.h5".format(MODEL_PATH))

if __name__ == "__main__":
    main()