const aws = require("aws-sdk");

const dynamoDB = new aws.DynamoDB.DocumentClient({
  region: "us-east-1",
  apiVersion: "2012-08-10",
});

exports.handler = async (event) => {
  try {
    console.log("event: ", event);

    const { Records } = event;

    const body = JSON.parse(Records[0].body);

    console.log("Incoming message body from SQS :", body);

    const params = {
      TableName: "test-dynamo-table1",
      Item: {
        userId: body.userId,
        name: body.name,
        age: body.age,
      },
    };

    await dynamoDB.put(params).promise();

    console.log("Successfully written to DynamoDB");
  } catch (error) {
    console.error("Error in executing lambda: ", error);
    return { statusCode: 500, "message:": "Error while execution" };
  }
};
