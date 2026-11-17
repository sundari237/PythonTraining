import boto3

session = boto3.Session()

print("Profile:", session.profile_name)
print("Region:", session.region_name)
print("Credentials:", session.get_credentials())