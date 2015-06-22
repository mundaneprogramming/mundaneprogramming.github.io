import boto3
from os import environ
from os.path import expanduser
from posixpath import join as posixpathjoin
from boto.s3.connection import OrdinaryCallingFormat
from boto.s3.key import Key as S3Key
from boto import connect_s3

CONN_DEFS = {
    'aws_access_key_id': environ.get('AWS_ACCESS_KEY_ID'),
    'aws_secret_access_key': environ.get('AWS_SECRET_ACCESS_KEY'),
     'calling_format': OrdinaryCallingFormat(),
     'region_name': 'us-east-1'
}

OPT_DEFS = {
    'bucket_name': 'www.mundaneprogramming.com',
    'start_path': 'stowy',
}




# http://boto.readthedocs.org/en/latest/ref/s3.html
# http://boto.readthedocs.org/en/latest/s3_tut.html

# https://github.com/boto/boto/issues/2836#issuecomment-77612836
def get_s3_conn(aws_access_key_id, aws_secret_access_key, calling_format, region_name):
    conn = boto.s3.connect_to_region(region_name = region_name,
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    calling_format=calling_format)
    return conn


def get_s3_bucket(conn, bucket_name):
    bucket = conn.create_bucket(bucket_name)
    return bucket

def resolve_filepath(path):
    return path

def upload_single_file(file, bucket, keyname):
    thekey = S3Key(bucket)
    thekey.key = keyname
    txt = file.read()
    # thekey.set_contents_from_string('This is a test of S3')


def stowy(path_to_stow, bucket_name = OPT_DEFS['bucket_name'],
            start_path = OPT_DEFS['start_path'],
            conn = get_s3_conn(**CONN_DEFS),
            use_basename = True
            ):
    bucket = get_s3_bucket(conn, bucket_name)
    fname = basename(path_to_stow) if use_basename else path_to_stow
    keyname = posixpathjoin(start_path, fname)

    ## TODO
    # upload_single_file(open(path_to_stow), bucket, keyname)



path, options = DEFAULTS
