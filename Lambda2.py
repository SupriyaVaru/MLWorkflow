from sagemaker.serializers import IdentitySerializer

# Fill this in with the name of your deployed model
endpoint = "image-classification-2023-02-10-15-21-17-347" ## TODO: fill in
session = sagemaker.Session()

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['body']['image_data'])## TODO: fill in

    # Instantiate a Predictor
    predictor = sagemaker.predictor.Predictor(
                        endpoint,
                        sagemaker_session=session,
                        serializer=sagemaker.serializers.IdentitySerializer()
                    )## TODO: fill in

    # For this model the IdentitySerializer needs to be "image/png"
    predictor.serializer = IdentitySerializer("image/png")
    
    # Make a prediction:
    inferences = predictor.predict(image)## TODO: fill in
    
    # We return the data back to the Step Function    
    event["inferences"] = inferences.decode('utf-8')
    return {
        'statusCode': 200,
        'body': {
            "image_data": event['body']['image_data'],
            "s3_bucket": event['body']['s3_bucket'],
            "s3_key": event['body']['s3_key'],
            "inferences": event["inferences"]
        }
    }