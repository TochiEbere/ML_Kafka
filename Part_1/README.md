## INTRODUCTION
This is a CNN pipeline for classifying images.  
While this pipeline may be used for several image datasets, the default dataset it trains on is the Fashion Mnist dataset.  

The folder contains the following:  
1. CNN_pipeline.py - Contains a CNNPipeline class with the following methods:  
    i. *model_architechture*: compiles a pre-defined CNN architechture.  
    ii. *train_CNNmodel*: for traning a CNN model.  
    iii. *model_accuracy*: for displaying the model train and validation accuracy results.  
2. main.py: An executable script for training the CNN model.

## How to run it  
#### Step 1: Install program requirements

```bash
pip3 install -r requirements.txt
```
#### Step 2: Run main.py  

This accepts the following command line arguments:  
i. --model_path (str, required): File path to save the model at
ii. --data_source (str): Either of 'custom' or 'fashion_mnist'. Default is 'fashion_mnist
iii. --num_classes (int, optional): Number of classes in train data. Defaults to 10 (Assuming it's a fashion mnist dataset)
iv. --target_size (int, optional): Dimension to which input image will be resized. Default is 28
v. --data_dir (str, optional): Directory where train data is stored. Should contain sub directories, where each directory contains a class. Deafult is 'None'.  
   When set to the default value, train data used is the fashion_mnist dataset from tensorflow_datasets
vi. --num_epoch (int, optional): number of epochs. Default is 10

#### Training the model on fashion_mnist data
```bash
python .\Part_1\main.py --model_path='path to save the model' --data_source='fashion_mnist'
```

#### Training the model on custom data
```bash
python .\Part_1\main.py --model_path='path to save the model' --data_source='custom' --num_classes='number of classes' --data_dir='train data directory' --num_epoch=10
```


