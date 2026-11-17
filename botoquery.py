import boto3

session = boto3.Session(profile_name="moj")
athena = session.client(
    "athena",
    region_name="eu-west-2"
)

response = athena.start_query_execution(
    QueryString="""
        SELECT *
        FROM names
        LIMIT 10
    """,
    QueryExecutionContext={
        "Database": "addresses"
    },
    ResultConfiguration={
        "OutputLocation": "s3://YOUR-QUERY-RESULTS-BUCKET/"
    }
)

print(response["QueryExecutionId"])