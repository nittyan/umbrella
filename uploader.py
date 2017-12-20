import boto3


class Uploader(object):

    def __init__(self, bucket_name):
        self._bucket = self._get_bucket(bucket_name)

    def _get_bucket(self, bucket_name):
        s3 = boto3.resource('s3')
        return s3.Bucket(bucket_name)
        
    def upload(self, local_path, upload_path):
        self._bucket.put_object(
            ACL='public-read',
            Key=upload_path,
            Body=open(local_path, 'rb'),
            ContentType='image/jpeg')

    
