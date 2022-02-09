from PIL import Image
import numpy as np
from tensorflow.keras.models import Sequential, save_model, load_model
import tensorflow as tf
from utils import parse_args
import tensorflow_datasets as tfds
import json
import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Parses args to CNN pipeline", 
        allow_abbrev=False)

    parser.add_argument('--image_path', type=str,
                        help='Full path to image')
    
    parser.add_argument('--labels', type=str,
                        help='Json file of labels')

    parser.add_argument('--model_path', type=str,
                        help='Full path to CNN model')

    parser.add_argument('--target_size', type=int,
                        default=28,
                        help='Dimension to which input image will be resized')  
    
    parser.add_argument('--data_source', type=str,
                        default='fashion_mnist',
                        help='Either fashion_mnist or custom')
    
    args = parser.parse_args()
    return args


def load_data(image_path, target_size):
    img = Image.open(image_path)
    img = img.resize((target_size,target_size))
    np_img = np.array(img)
    np_img = tf.cast(np_img, tf.float32) / 255.
    np_img = np.expand_dims(np_img, axis=0)
    return np_img

def stream_data():
    data = 