## Step to follow

1. Create a Kinesis Data fire hose delivery stream.
2. Do not enable the option of "Convert record format" in Kinesis Data fire hose delivery stream.
3. And Enable dynamic partitioning in Kinesis Data fire hose delivery stream.
4. Create a S3 bucket to store data from Kinesis Data fire hose.
5. Add a s3 bucket to the Kinesis Data fire hose delivery stream.

## Note

1. If you enable the option of "Convert record format" in Kinesis Data fire hose delivery stream then you have to add a lambda function to convert the data in json format.
2. Dont enable encryption in Kinesis Data fire hose delivery stream.
3. Change the buffer size and buffer interval according to your requirement.
4. When creating a data firehorse add these line to daynamic pratioting option.

```bash
customer_id=!{partitionKeyFromQuery:customer_id}/
```

## How to run the code

1. Create a virtual environment.
2. Create a .env file and a aws credential to it and aws region.
3. Change the name of the delivery stream in the code.
4. Run the code.
5. Check the data in the S3 bucket.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.
