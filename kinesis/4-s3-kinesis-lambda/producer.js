const AWS = require("aws-sdk");

AWS.config.update({
  region: "us-east-1",
});

const s3 = new AWS.S3();
const kinesis = new AWS.Kinesis();

exports.handler = async (event) => {
  console.log(JSON.stringify(event));
  const bucketName = event.Records[0].s3.bucket.name;
  const keyName = event.Records[0].s3.object.key;
  const params = {
    Bucket: bucketName,
    Key: keyName,
  };

  await s3
    .getObject(params)
    .promise()
    .then(
      async (data) => {
        const dataString = data.Body.toString();
        const payload = {
          data: dataString,
        };
        await sendToKinesis(payload, keyName);
      },
      (Error) => {
        console.log(Error);
      }
    );
};

async function sendToKinesis(payload, partitionKey) {
  const params = {
    Data: JSON.stringify(payload),
    PartitionKey: partitionKey,
    StreamName: "game-data-stream",
  };
  try {
    await kinesis.putRecord(params).promise();
  } catch (error) {
    console.log(error);
  }
}
