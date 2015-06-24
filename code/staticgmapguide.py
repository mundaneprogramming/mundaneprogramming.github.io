from requests import Request
from string import ascii_uppercase
GMAP_STATIC_ENDPOINT = 'https://maps.googleapis.com/maps/api/staticmap'
COLOR_IMPORTANT = "red"
COLOR_DEFAULT = "purple"


def make_markers(items, labels = ascii_uppercase):
    """
    items is a list
    returns a list of strings:
        "color:red|label:'A'|-42.2,42.2"
        "color:purple|label:'B'|Stanford,CA"
    """
    markers = []
    for idx, i in enumerate(items):
        m = []
        if not i.get('color'):
            i['color'] = COLOR_IMPORTANT if i.get('important') else COLOR_DEFAULT
        m.append('color:%s' % i['color'])
        # label
        m.append('label:%s' % labels[idx])

        if i.get('lat'): # coordinates
            m.append("%s,%s" % (i['lat'], i['lng']))
        else:
            m.append(i['location'])
        markers.append('|'.join(m))
    return markers

def make_path(items, path_styles = {}):
    paths = []
    for i in items:
        p = ("%s,%s" % (i['lat'], i['lng'])) if i.get('lat') else i['location']
        paths.append(p)
    # todo path styles
    return '|'.join(paths)



def map_maker(items, size = "600x400"):
    """
    items is a list
    Each item is a dict:
    { 'lat': -42.2, 'lng': 42.2 }
    { 'location': "Stanford,CA", important = True }
    """
    gmap = {}
    gmap['size'] = size
    gmap['markers'] = make_markers(items)
    gmap['path'] = make_path(items)

    req = Request('get', url = GMAP_STATIC_ENDPOINT, params = gmap)
    preq = req.prepare()
    return preq.url
