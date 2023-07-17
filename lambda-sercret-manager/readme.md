## Steps to use the code in this repository

1. Clone the repository to your local machine
2. Open the project in your IDE
3. Then login to your AWS account and create a new IAM user with programmatic access and attach the AdministratorAccess policy to it.
4. Then copy the access key and secret key and paste it in the credentials file in your local machine.
5. Then Go to RDS and create a new database instance with Mysql as the database engine and give the username and password of your choice.
6. Then go to Secrets Manager and create a new secret and select the credentials of the database instance you created in the previous step.
7. Then Do the following steps:
   1. Lambda and create Function of any name and select Nodejs 16.0 as the runtime.
   2. Then Copy The main.js code from the repository and paste it in the lambda function.
   3. Then edit the iam role of the lambda function
   4. Then add the following policies to the role:
      1. AWSLambdaBasicExecutionRole
      2. AWSLambdaVPCAccessExecutionRole
      3. AmazonRDSFullAccess
      4. AmazonSecretsManagerReadWrite
8. And Finally test the lambda function by giving the following input:
   ```json
   {
     "username": "admin",
     "password": "admin"
   }
   ```
9. And Go to cloudwatch logs to see the output of the lambda function.
10. And Finally go to the RDS database instance and see the data in the database.
