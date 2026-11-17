import boto3

athena = boto3.client(
    "athena",
    region_name="eu-west-2"
)

print(athena.list_work_groups())