# ML Workflow For Scones Unlimited On Amazon SageMaker. 
**ML Workflow** is the notebook for this project.

This project is based on CIFAR 100 dataset to classify motorcycles and bicycles. This has 4 stages.
## 1) Data Staging: 
Using Sage maker Studio, extracted the data from the hosting service. Data is encoded in binary format and then transformed(decoded) into the correct shape and format, loaded data into S3 bucket.
## 2)Model Training and Deployment:
Used AWS build-in image classification algorithm to train the model. Trained model is then deployed to an endpoint and configured Model Monitor to track the deployment. Then made an inference to test the model endpoint.
## 3)Lambdas and Step Function Workflow: 
Created three lambda functions: 
Lambda1.py is responsible for data generation. 
Lambda2.py is responsible for image classification. 
Lambda3.py is responsible for filtering out low-confidence inferences. 
And using Step Functions streamed the workflow of these lambda functions. It is exported as workflow.asl(1).json
## 4) Testing and Evaluation: 
Performed several step function invocations using data from the test dataset. This process should has given me confidence that the workflow both succeeds AND fails as expected. In addition, used captured data from SageMaker Model Monitor to create a visualization to monitor the model.

## Screenshots of workflow with logs:

Workflow when succeeded with event status:

![stepfunctions_graph_succeeded](https://user-images.githubusercontent.com/103468158/220775633-1a5469f9-baa9-4291-a300-6fe8dff23570.png)

![stepfunctionsucceeded](https://user-images.githubusercontent.com/103468158/220775925-1536943f-b492-4c77-89d6-360314cda614.png)

Workflow when failed with event status:

![stepfunctions_graph_failed](https://user-images.githubusercontent.com/103468158/220775771-2db762f4-b74a-4eee-a151-c56c74aa77d9.png)

![stepfunctionFailed_lowThreshold](https://user-images.githubusercontent.com/103468158/220775813-77164e1c-05c8-4552-9d71-3f51c8c32ce2.png)
