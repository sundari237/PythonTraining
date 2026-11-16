import boto3

session = boto3.Session(profile_name="moj")

s3 = session.client("s3")

print("Connected to AWS")

try:
    response = s3.list_buckets()

    print("Response received")

    print(response)

    if "Buckets" in response:
        print(f"Buckets found: {len(response['Buckets'])}")

        for bucket in response["Buckets"]:
            print(bucket["Name"])

except Exception as e:
    print("Error:")
    print(e)