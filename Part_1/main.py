import numpy as np
from CNN_pipeline import CnnPipeline
from kafka_produce_consume import write_to_kafka, decode_kafka_item
from utils import parse_cnn_args, data_generator
# import tensorflow_io as tfio
import tensorflow as tf


def main():

    args = parse_cnn_args()
    MODEL_PATH = args.model_path
    DATA_SOURCE = args.data_source
    TARGET_SIZE = args.target_size
    NUM_CLASSES = args.num_class
    DATA_DIRECTORY = args.data_dir
    TARGET_SIZE = args.target_size
    OPTIMIZER="adam"
    LOSS = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

    train_data, test_data = data_generator(
        source=DATA_SOURCE,
        data_dir=DATA_DIRECTORY,
        target_size=TARGET_SIZE
        )

    model_pipeline = CnnPipeline(train_data, test_data)
    model_pipeline.model_architecture(TARGET_SIZE, NUM_CLASSES, OPTIMIZER, LOSS)
    cnn_model = model_pipeline.train_CNNmodel()
    model_pipeline.model_accuracy()
    cnn_model.save("{}.h5".format(MODEL_PATH))

if __name__ == "__main__":
    main()