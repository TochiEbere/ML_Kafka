import tensorflow as tf
from keras import datasets, layers, models
import matplotlib.pyplot as plt
# import scipy

# Helper libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils import parse_args


class CnnPipeline:

    def __init__(self, train_data, test_data):
         
        self.train_data = train_data
        self.test_data = test_data
        
    def model_architecture(self, target_size, num_class, optimizer, loss):            
        
        INPUT_SHAPE = (target_size, target_size, 1)
        METRICS = ['accuracy']

        model = models.Sequential()
        model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=INPUT_SHAPE))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(layers.Flatten())
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(num_class))
        model.compile(optimizer=optimizer, loss=loss, metrics=METRICS)
        self.model_arch = model
        # return model

    def train_CNNmodel(self,):
        cnn_model = self.model_arch
        history = cnn_model.fit(self.train_data, epochs=2, 
                    validation_data=self.test_data)
        self.model_history = history
        self.model = cnn_model
        return cnn_model      

    def model_accuracy(self):
        history = self.model_history
        # train_scores = model.evaluate(self.train_data) 
        # val_scores = model.evaluate(self.test_data)   
        print('Train accuracy score is:', history.history)    
        print('Test accuracy score is:', history.history['val_sparse_categorical_accuracy'][-1])    