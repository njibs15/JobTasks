from re import A
import boto3

s3_client = boto3.client('s3')



response = s3_client.create_bucket(
    ACL='private',
    Bucket= 'my-bucket-aris'
)
lfc = {
        "Rules": [
            {
                "Expiration": {"Days": 14},
                "ID": "wholebucket",
                "Filter": {"Prefix": ""},
                "Status": "Enabled",
            }
        ]
    }
s3_client.put_bucket_lifecycle_configuration(
        Bucket="my-bucket-aris", LifecycleConfiguration=lfc
    )
notify = {
            
}

s3_client.put_bucket_notification(
        Bucket="my-bucket-aris", NotificationConfiguration=notify
    )
s3_client.put_public_access_block(
    Bucket='my-bucket-aris',
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': True,
    }
)
print(response)