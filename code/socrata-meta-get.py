import posixpath
import requests
from os.path import splitext
from collections import OrderedDict
from urllib.parse import urljoin, urlparse, urlunparse

"""
get_meta(url) returns a simplified, summarized version of a
Socrata dataset's metadata, allowing a user to get

"""


# http://dev.socrata.com/docs/endpoints.html
def get_resource_meta(url):
    """
    returns:
        a Dict
    from:
        https://data.seattle.gov/dataset/City-of-Seattle-Events/cprz-jsz8
    to:
        https://data.seattle.gov/metadata/v1/dataset/kjqu-s8f9.json
    """
    p = get_resource_parts(url)
    path = posixpath.join('metadata', 'v1', p['type'], p['id'] + '.json')
    r_url = urljoin(p['base'], path)
    return requests.get(r_url).json()


def get_resource_views_meta(url):
    """
    returns:
        a List
    from:
        https://data.seattle.gov/dataset/City-of-Seattle-Events/cprz-jsz8
    to:
        https://data.seattle.gov/views/cprz-jsz8
    """
    p = get_resource_parts(url)
    path = posixpath.join('views', p['id'] + '.json')
    r_url = urljoin(p['base'], path)
    return requests.get(r_url).json()



def get_resource_parts(url):
    """
    returns: a Dict
    turn this:
        https://data.seattle.gov/dataset/City-of-Seattle-Events/cprz-jsz8
    into:
        {
            'base': 'https://data.seattle.gov',
            'id': 'cprz-jsz8',
            'type': 'dataset'
        }
    """
    parts = {}
    scheme, netloc, path, params, query, fragment = urlparse(url)
    # an elaborate of just getting:
    # https://data.seattlegov
    parts['base'] = urlunparse((scheme, netloc, '', '', '', ''))
    parts['type'] = path.split('/')[1]
    parts['id'] = splitext(path)[0].split('/')[-1]
    return parts


# http://stackoverflow.com/questions/27823200/is-there-a-socrata-api-method-to-get-the-row-count-of-a-dataset
def get_dataset_row_count(url):
    """
    returns: an Int
    # https://data.seattle.gov/resource/cprz-jsz8.json?$select=count(*)
    """
    r_url = resource_url(url) + '.json'
    j = requests.get(r_url, params = {'$select': 'count(*)'}).json()
    # [{'count': '3133'}]
    return int(j[0]['count'])

def resource_url(url):
    """
    return a String
    turn this:
        https://data.seattle.gov/dataset/City-of-Seattle-Events/cprz-jsz8
    into:
        https://data.seattle.gov/resource/cprz-jsz8
    """
    parts = get_resource_parts(url)
    path = posixpath.join('resource', parts['id'])

    return urljoin(parts['base'], path)



def get_meta(url):
    m = OrderedDict()
    xm = get_resource_views_meta(url)
    cols = xm['columns']
    m['name'] = xm['name']
    m['id'] = xm['id']
    m['nrows'] = get_dataset_row_count(url)
    m['ncols'] = len(cols)
    m['max_bytes'] = m['nrows'] * m['ncols'] # TODO

    m['updated_at'] = xm['rowsUpdatedAt']
    m['published_at'] = xm['publicationDate']
    m['download_count'] = xm['downloadCount']
    m['comment_count'] = xm['numberOfComments']
    m['view_count'] = xm['viewCount']
    m['description'] = xm['description']
    m['column_names'] = [c['fieldName'] for c in cols]

    return m



# def get_domain_datasets(url):
#     urlj = urljoin(url, 'data.json')
#     data = requests.get(urlj).json()
#     return data['dataset']



## CLI TODO
