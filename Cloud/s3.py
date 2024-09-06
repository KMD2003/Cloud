import boto3

# Initialize a session using your preferred region
session = boto3.Session(region_name='us-west-2')  # Replace 'us-west-2' with your actual region
s3 = session.resource('s3')

# List all S3 buckets
print("Listing S3 Buckets:")
for bucket in s3.buckets.all():
    print(bucket.name)

bucket_name = 'shreesha-bucket-17'

# Create an S3 bucket with the specified region
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2'  # Ensure this matches your region
    }
)
print(f"Bucket {bucket_name} created.")

# Upload a file to the S3 bucket
s3.Bucket(bucket_name).upload_file('Screenshot 2024-07-04 192117.png', 'image1.png')
print("File uploaded.")

# Download the file from the S3 bucket
s3.Bucket(bucket_name).download_file('image1.png', 'newimage.png')
print("File downloaded.")

# Delete the file from the S3 bucket
s3.Object(bucket_name, 'image1.png').delete()
print("File deleted.")

# Delete the S3 bucket
s3.Bucket(bucket_name).delete()
print(f"Bucket {bucket_name} deleted.")
