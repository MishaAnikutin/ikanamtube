from django.test import TestCase

from ikanamtube.settings import (
    AWS_S3_ENDPOINT_URL,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
)

import boto3


class TestS3Connection(TestCase):
    def setUp(self):
        self.s3 = boto3.client(
            "s3",
            endpoint_url=AWS_S3_ENDPOINT_URL,
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )

    def test_s3_connection(self):
        self.s3.list_buckets()
