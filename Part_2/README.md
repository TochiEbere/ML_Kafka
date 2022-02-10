## PART 2

This is a unified API for streaming data asynchornously using either Apache Kafka or Google Pubsub.  

The folder contains the following:

The folder contains the following:  
1. uitls.py - Contains utility functions such as command line arguments
2. stream_event.py - Contains a parent class *StreamRequest* and 2 child classes *KafkaStream and GooglePubsub*. with the following methods:  
    i. *produce*: A method that starts a producer instance  
    ii. *consume*: A method that starts a consumer instance  
    iii. *data_encoder*: A data serializer  
3. consumer.py: Calls a consumer instance
4. producer.py: Calls a producer instance 

## How to run it  
#### Step 1: Create a topic on Kafka or Google Pubsub  
#### Step 2: Create a subscriber to consume data on Google Pubsub

#### Step 3: Start a consumer instance by running consumer.py  
This accepts the following command line arguments:  
i. --broker_type (str): Either of kafka or Google Pubsub. Defaults to "kafka"  
ii. --topic_name (str, compulsory): Topic name  
iii. --gcp_credentials (str, optional): GCP credentials (Not required if --broker_type='kafka)  
iv. --subscription_id (str, optional): GCP subscriber Subscription ID (Not required if --broker_type='kafka)  
v. --project_id (str, optional): GCP project ID (Not required if --broker_type='kafka)

```bash
python .\Part_2\consumer.py --topic_name='topic name'
```

#### Step 4: Start a consumer instance by running producer.py  
This accepts the following command line arguments:  
i. --broker_type (str, compulsory): Either of kafka or Google Pubsub. Defaults to "kafka"  
ii. --topic_name (str, compulsory): Topic name   
iii. --image_path (str, compulsory): path to image data to be streamed  
iv. --gcp_credentials (str, optional): GCP credentials (Not required if --broker_type='kafka)  
v. --project_id (str, optional): GCP project ID (Not required if --broker_type='kafka)

```bash
python .\Part_2\producer.py --image_path="Path to image data" --topic_name='Topic name'
```

