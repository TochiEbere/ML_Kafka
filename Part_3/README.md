## PART 3

Data streaming via Apache Kafka in to a machine learning model for prediction.

The folder contains the following:

The folder contains the following:  
1. uitls.py - Contains utility functions such as command line arguments
2. stream_event.py - Contains a parent class *StreamRequest* and 2 child classes *KafkaStream and GooglePubsub*
3. consumer.py: Calls a consumer instance
4. main.py: An executable script to consume data from a running producer and feed it into a CNN model for prediction. Returns the predicted class.

## How to run it 
#### Step 3: Start a consumer instance by running consumer.py  
This accepts the following command line arguments:  
i. --broker_type (str): Either of kafka or Google Pubsub. Defaults to "kafka"  
ii. --topic_name (str, compulsory): Topic name  
iii. --gcp_credentials (str, optional): GCP credentials (Not required if --broker_type='kafka)  
iv. --subscription_id (str, optional): GCP subscriber Subscription ID (Not required if --broker_type='kafka)  
v. --project_id (str, optional): GCP project ID (Not required if --broker_type='kafka)  
vi. --model (str, compulsory): path to pre-trained model  
vii. --labels (str): Path to Json file of label names. Must be specified if model was not trained on a fashion)mnist dataset  
viii. --data_source (str, compulsory): Data source. Either of 'fashion_mnist' or 'custom'  


```bash
python .\Part_3\main.py  --topic_name='topic name' --model='model path' 
```
