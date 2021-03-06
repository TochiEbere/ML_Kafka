## PART 3

Data streaming via Apache Kafka in to a machine learning model for prediction.

The folder contains the following:

The folder contains the following:  
    main.py: An executable script to consume data from a running producer and feed it into a CNN model for prediction. Returns the predicted class.

## How to run it 
### Step 1: Run main.py  
This accepts the following command line arguments:  
i. --broker_type (str): Either of kafka or Google Pubsub. Defaults to "kafka"  
ii. --topic_name (str, required): Topic name  
iii. --gcp_credentials (str, optional): GCP credentials (Not required if --broker_type='kafka)  
iv. --subscription_id (str, optional): GCP subscriber Subscription ID (Not required if --broker_type='kafka)  
v. --project_id (str, optional): GCP project ID (Not required if --broker_type='kafka)  
vi. --model (str, required): path to pre-trained model  
vii. --labels (str): Path to Json file of label names. Must be specified if model was not trained on a fashion)mnist dataset  
viii. --data_source (str, required): Data source. Either of 'fashion_mnist' or 'custom'  


```bash
python .\Part_3\main.py  --topic_name='topic name' --model='model path' 
```

### Step 2: On a separate terminal run producer.py
This accepts the following command line arguments:  
i. --broker_type (str, required): Either of kafka or Google Pubsub. Defaults to "kafka"  
ii. --topic_name (str, required): Topic name   
iii. --image_path (str, required): path to image data to be streamed  
iv. --gcp_credentials (str, optional): GCP credentials (Not required if --broker_type='kafka)  
v. --project_id (str, optional): GCP project ID (Not required if --broker_type='kafka)

```bash
python .\Part_2\producer.py --image_path="Path to image data" --topic_name='Topic name'
```
