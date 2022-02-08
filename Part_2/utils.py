import argparse
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras import datasets, layers, models
import tensorflow_datasets as tfds

def parse_cnn_args():

    cnn_parser = argparse.ArgumentParser(
        description="Parses args to CNN pipeline", 
        allow_abbrev=False)

    cnn_parser.add_argument('--data_source', type=str,
                        default='fashion_mnist',
                        help='Either fashion_mnist or custom')

    cnn_parser.add_argument('--data_dir', type=str,
                        default=None,
                        help='Directory path to data')

    cnn_parser.add_argument('--target_size', type=int,
                        default=28,
                        help='Dimension to which input image will be resized')  

    cnn_parser.add_argument('--num_class', type=int,
                        default=10,
                        help='Number of classes') 

    cnn_parser.add_argument('--model_path', type=str,
                        default='model',
                        help='Path to save the model')

    args = cnn_parser.parse_args()
    return args


def parse_broker_args():
    broker_parser = argparse.ArgumentParser(
            description="Parses args to message broker", 
            allow_abbrev=False)

    broker_parser.add_argument('--broker_type', type=int,
                                default='kafka', 
                                help='Broker type to use. Options are kafka or googlepubsub')

    broker_parser.add_argument('--topic_name', type=int,
                                help='Topic name')

    broker_parser.add_argument('--image_path', type=str,
                                help='Full path to image file')

    broker_parser.add_argument('--gcp_credentials', type=str,
                                default=None,help='Full path to GCP credentials')
    
    broker_parser.add_argument('--project_id', type=str,
                                default=None, help='GCP service account project ID')

    broker_parser.add_argument('--subscription_id', type=str,
                                default=None, help='Subscrition ID of Google Pubsub consumer')
    
    args = broker_parser.parse_args()
    return args


def data_generator(source, data_dir=None, target_size=None):

    if source=='fashion_mnist':
        # Load fashion mnist dataset
        print("""Loading fashion mnist data from tensorflow""")
        train, test = tfds.load(
            "fashion_mnist", 
            split=["train", "test"],
            shuffle_files=True,
            as_supervised=True,)
        
        # Normalizing the dataset
        def normalize_img(image, label):
            """Normalizes images: `uint8` -> `float32`."""
            return tf.cast(image, tf.float32) / 255., label

        train = train.map(normalize_img, num_parallel_calls=tf.data.AUTOTUNE)
        test = test.map(normalize_img, num_parallel_calls=tf.data.AUTOTUNE)
        train = train.batch(32)
        test = test.batch(32)
        
        return train, test

    else:
        # Load command line arguments
        args = parse_cnn_args()
        # DATA_DIRECTORY = args.data_dir
        # TARGET_SIZE = args.target_size

        # Generate custom train data
        datagen = ImageDataGenerator(rescale = 1./255, validation_split=0.2)
        train_data_generator = datagen.flow_from_directory(
            data_dir,
            target_size = (target_size, target_size),
            class_mode = 'sparse',
            color_mode='grayscale',
            shuffle = True,
            subset='training'
            )

        # Generate custom test data        
        test_data_generator = datagen.flow_from_directory(
            data_dir,
            target_size = (target_size, target_size),
            class_mode = 'sparse',
            color_mode='grayscale',
            shuffle = True,
            subset='validation'
            )
    
        return train_data_generator, test_data_generator
