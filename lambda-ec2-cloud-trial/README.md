### This file is demosnstating how to use main.py file to run the program and get the results.

1.  Then go to cloudtrial and create one trail and one bucket.
2.  Then go to event bridge and create one rule and one target.
3.  Then go to lambda and create one function.
4.  Then Clone the repo from github.
5.  Then go to the main.py file and change the bucket name and the trail name.
6.  Then go to the lambda and upload the main.py file.
7.  Then go to the event bridge and change the target to the lambda function.
8.  Then add following policy to the iam role of the lambda function

    1.  Create a Inline policy Followed by the below policy
    2.  {
        "Version": "2012-10-17",
        "Statement": [
        {
        "Sid": "VisualEditor1",
        "Effect": "Allow",
        "Action": [
        "cloudtrail:LookupEvents",
        "cloudtrail:DescribeTrails",
        "cloudtrail:GetTrailStatus",
        "cloudtrail:GetTrail",
        "cloudtrail:ListTrails",
        "cloudtrail:ListPublicKeys",
        "cloudtrail:GetEventSelectors",
        "cloudtrail:GetEventSelec tor",
        "cloudtrail:ListTags",
        "cloudtrail:GetTrailStatus",
        "cloudtrail:GetTrail",
        "cloudtrail:DescribeTrails",
        "cloudtrail:LookupEvents",

                    ],
                    "Resource": "*"
                }
            ]

        }

9.  And Also for the lambda function add the following policy to the iam role of the lambda function

    1.  Create a Inline policy Followed by the below policy
    2.  {
        "Version": "2012-10-17",
        "Statement": [
        {
        "Sid": "VisualEditor1",
        "Effect": "Allow",
        "Action": [
        "events:PutEvents",
        "events:PutRule",
        "events:PutTargets",
        "events:RemoveTargets",
        "events:DeleteRule",
        "events:DescribeRule",
        "events:ListTargetsByRule",
        "events:ListRules",
        "events:ListRuleNamesByTarget",
        "events:TestEventPattern",
        "events:ListEventBuses",
        "events:ListEventSources",
        "events:DescribeEventBus",
        "events:DescribeEventSource",
        "events:PutPermission",
        "events:RemovePermission",
        "events:DescribeEventBus",
        "events:PutPartnerEvents",
        "events:PutEvents",
        "even ts:PutPartnerEvents",

                    ],
                    "Resource": "*"
                }
            ]

        }

10. Then add a ec2 tag policy to the iam role of the lambda function 1. Create a Inline policy Followed by the below policy 2. {
    "Version": "2012-10-17",
    "Statement": [
    {
    "Sid": "VisualEditor1",
    "Effect": "Allow",
    "Action": "ec2:CreateTags",
    "Resource": "*"
    }
    ]
    }

### This how its works
