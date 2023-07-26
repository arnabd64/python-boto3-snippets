import boto3




class S3:
    
    def __init__(self):
        self.client = boto3.client("s3")
        
        
    def listAllBuckets(self):
        r = self.client.list_buckets()
        return [bucket["Name"] for bucket in r["Buckets"]]
    
    
    def listAllObjects(self, bucket_name: str):
        try:
            r = self.client.list_objects(Bucket = bucket_name)
            return [object["Key"] for object in r["Contents"]]

        except Exception as e:
            print("ERROR: " + str(e))
            return None
    
    
