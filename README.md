# Code Snippets for `boto3`

`boto3` is the official Python SDK for Amazon Web Services. The `boto3` package provides an interface for using AWS programmetically. To get started with `boto3`, you need to have the following packages installed:

```python
awscli == 1.29
boto3 == 1.28
```

+ `awscli` handles the backend the backend requests and user authentication.
+ `boto3` provides api's to communicate with AWS.

## STEP 1: Setting up User Authentication using `awscli`

Obtain the __AWS Access Key__ and the __Secret Key__ from IAM. You can do it by yourself or ask the Cloud Admin to provide the needed keys. You can refer to this [YouTube video](https://www.youtube.com/watch?v=HuE-QhrmE1c)

Then open your terminal and execute the following command

```bash
$ aws configure
```

`awscli` will ask for __Access Key__ and __Secret Key__, fill iy in and also set the `default output` to `json`.

## STEP 2: Check if `boto3` is working

Copy paste this simple code that creates a __S3 Bucket__ and see if it executes correctly

```python
import boto3

# create a client for S3
s3_client = boto3.client("s3")

# create a bucket
response = s3_client.create_bucket(
    Bucket = "my-demo-bucket",
    CreateBucketConfiguration = dict(LocationConstraint = "ap-south-1")
)

# display the response
print(response)
```
 If the above code comes out as a success then you have correctly configured the SDK.