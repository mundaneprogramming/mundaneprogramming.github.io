import boto3
from os import environ
from os.path import expanduser, basename
from posixpath import join as posixpathjoin
from boto.s3.connection import OrdinaryCallingFormat
from boto.s3.key import Key as S3Key
from urllib.parse import urlsplit
import boto.s3

CONN_DEFS = {
    'aws_access_key_id': environ.get('AWS_ACCESS_KEY_ID'),
    'aws_secret_access_key': environ.get('AWS_SECRET_ACCESS_KEY'),
     'calling_format': OrdinaryCallingFormat(),
     'region_name': 'us-east-1'
}

OPT_DEFS = {
    'bucket_name': 'www.mundaneprogramming.com',
    'prepend_path': ''
}

# http://boto.readthedocs.org/en/latest/ref/s3.html
# http://boto.readthedocs.org/en/latest/s3_tut.html

# https://github.com/boto/boto/issues/2836#issuecomment-77612836


def get_file_bytes(path):
    # check to see if remote URL
    if 'http' in urlsplit(path).scheme:
        f = requests.get(BytesIO(resp.content))
    else:
        f = open(path, 'rb')
    return f


def get_s3_bucket(conn, bucket_name):
    bucket = conn.create_bucket(bucket_name)
    return bucket

def get_s3_conn(aws_access_key_id, aws_secret_access_key, calling_format, region_name):
    conn = connect_to_region(region_name = region_name,
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    calling_format=calling_format)
    return conn

def upload_single_file(file, bucket, keyname):
    # uploads the file without concern of an existing key
    # returns s3.key object
    thekey = S3Key(bucket)
    thekey.key = keyname
    thekey.set_contents_from_file(file)
    return thekey

# def stowy(path_to_stow, bucket_name = OPT_DEFS['bucket_name'],
#               prepend_path = OPT_DEFS['start_path'],
#               conn = get_s3_conn(**CONN_DEFS),
#               use_basename = True
#             ):
def stowy(path_to_stow, bucket_name, conn, prepend_path = "", use_basename = True):
    bucket = get_s3_bucket(conn, bucket_name)
    rfname = basename(path_to_stow) if use_basename else path_to_stow
    keyname = posixpathjoin(prepend_path, rfname)
    ## todo make better
    atts = {'bucket': bucket, 'keyname': keyname}
    atts['file'] = get_file_bytes(path_to_stow)
    resp = upload_single_file(**atts)
    return resp

