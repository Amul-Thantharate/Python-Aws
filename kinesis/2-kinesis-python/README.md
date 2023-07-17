## Create a fucntion for Kinesis Data Stream and Trigger the lambda function to process the data from Kinesis Data Stream

1 - Create a Kinesis Data Stream
2 - Create a Lambda function
3 - Create a IAM role for Lambda function
4 - Attach the IAM role to Lambda function
5 - Create a trigger for Lambda function
6 - Create a IAM role for Kinesis Data Stream
7 - Attach the iam role to lambda function

## Then Follow these step

1. clone the repo
2. cd into the repo
3. There will be two file
   1. lambda_function.py
   2. main.py
4. Run The main.py file from local terminal
5. Then go to the AWS console and check the lambda function logs

## Note:

1. You can change the name of the Kinesis Data Stream in the main.py file

## Output:

1. You will see the data from the Kinesis Data Stream in the lambda function logs
