from os import environ
from os.path import expanduser, basename
from posixpath import join as posixpathjoin
from urllib.parse import urlsplit
import boto3
import argparse
import requests
from io import BytesIO

CONN_DEFS = {
    'aws_access_key_id': environ.get('AWS_ACCESS_KEY_ID'),
    'aws_secret_access_key': environ.get('AWS_SECRET_ACCESS_KEY'),
     # 'calling_format': OrdinaryCallingFormat(),
     'region_name': 'us-east-1'
}

# http://boto.readthedocs.org/en/latest/ref/s3.html
# http://boto.readthedocs.org/en/latest/s3_tut.html
# https://github.com/boto/boto/issues/2836#issuecomment-77612836
def get_file_bytes(path):
    # check to see if remote URL
    if 'http' in urlsplit(path).scheme:
        f = BytesIO(requests.get(path).content)
    else:
        f = open(path, 'rb')
    return f


def get_s3_bucket(client, bucket_name, acl = 'public-read'):
    return client.create_bucket(Bucket = bucket_name, ACL = acl)




# def get_s3_key(bucket, key_name):
#     key = S3Key(bucket)
#     key.name = key_name
#     return key


def get_s3_client(aws_access_key_id, aws_secret_access_key, region_name):
    session = boto3.Session(aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  region_name=region_name)
    # client = boto.s3.clientect_to_region(region_name = region_name,
    #                 aws_access_key_id = aws_access_key_id,
    #                 aws_secret_access_key = aws_secret_access_key,
    #                 calling_format = calling_format)
    client = session.client('s3')
    return client

def upload_single_file(file, client, bucket, key, acl = 'private'):
    # dumb upload, expects all work to be done in the key
    resp = client.put_object(ACL = acl, Bucket = bucket, Body = file, Key = key)
    return resp

def stowy(path_to_stow,  client, bucket_name, key_name = None, prepend_path = "", use_basename = True):
    bucketresp = get_s3_bucket(client, bucket_name)
    # TODO: check bucketresp
    bucket = bucket_name
    if not key_name:
        key_name = basename(path_to_stow) if use_basename else path_to_stow
    key = posixpathjoin(prepend_path, key_name)
    f = get_file_bytes(path_to_stow)
    resp = upload_single_file(file = f, client = client, bucket = bucket,
        key = key_name, acl = 'public-read')
    return resp


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', '-f', nargs = 1,
        help ='Specify a local filename or URL pointing to a file')
    parser.add_argument('--bucket', '-b', nargs = 1,
        help ='Specify a bucket')

    args = parser.parse_args()
    a_filename = args.filename[0]
    a_bucketname = args.bucket[0]
    client = get_s3_client(**CONN_DEFS)
    # send file
    resp = stowy(path_to_stow = a_filename, client = client, bucket_name = a_bucketname)
    print(resp)
    # TODO: extract url
    # TODO: option to set limited expire
    # public_url = key.generate_url(expires_in = 0, query_auth = False, force_http = True)
    # print(public_url)
    # # TODO: option to set compression
    #  - Deal with local directories
    #  - Deal with wget site mirroring

