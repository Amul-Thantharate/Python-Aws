### This is the Data Stream Work in kinesis data stream using serverless framework and nodejs in AWS cloud platform

## Prerequisites

1. AWS Account
2. You must have install serverless framework in your local machine
3. You must have install aws cli in your local machine
4. You must have install nodejs in your local machine
5. And finally install serverless framework plugin in your local machine

## Installation

1. Clone the repository
2. cd into the directory
3. Then Run npm install
4. Then Run sls deploy -v or serverless deploy -v (if you have install serverless framework plugin)

## Usage

1. After successfully deploy the project then go to the AWS console and then go to the kinesis data stream
2. Go to lambda function and then go to the lambda function which is created by the serverless framework
3. Chage the Stream name in producer.js file name of your stream name
   ![alt text](And finally run the node producr.js file in your local machine)

4. Then go to the lambda function and go to the monitoring tab and then click on the view logs in cloudwatch
5. Then go to the cloudwatch and then go to the log group and then go to the log stream and then you can see the logs

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

```bash
MIT License
```
