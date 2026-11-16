import boto3

session = boto3.Session(profile_name="moj")

sts = session.client("sts")

print(sts.get_caller_identity())