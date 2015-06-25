---
title: Create a Google Static Maps Directions Sheet
---

https://maps.googleapis.com/maps/api/staticmap?center=Williamsburg,Brooklyn,NY&zoom=13&size=400x400&
markers=color:blue%7Clabel:S%7C11211%7C11206%7C11222

https://maps.googleapis.com/maps/api/staticmap?&markers=color:blue%7Clabel:A%7CBrooklyn,NY

path=color:0x0000ff|weight:5|40.737102,-73.990318|40.749825,-73.987963


[Documentation](https://developers.google.com/maps/documentation/staticmaps/
)

## Endpoint

    https://maps.googleapis.com/maps/api/staticmap


## Size

    size=400x400

## Markers


> Because both style information and location information is delimited via the pipe character, style information must appear first in any marker descriptor. Once the Static Map server encounters a location in the marker descriptor, all other marker parameters are assumed to be locations as well.

    markers=color:blue|label:A|Brooklyn,NY


All together:

https://maps.googleapis.com/maps/api/staticmap?size=400x400&markers=color:blue|label:A|Brooklyn,NY

## Multiple points

### Same marker style

    markers=color:blue|label:A|Brooklyn,NY|Brighton+Beach

https://maps.googleapis.com/maps/api/staticmap?size=400x400&markers=color:blue|label:A|Brooklyn,NY|Brighton+Beach,NY


### Different marker style

    markers=color:blue|label:A|Brooklyn,NY&markers=label:B|Brighton+Beach,NY


https://maps.googleapis.com/maps/api/staticmap?size=400x400&markers=color:blue|label:A|Brooklyn,NY&markers=label:B|Brighton+Beach,NY





## Paths

https://maps.googleapis.com/maps/api/staticmap?size=400x400&path=color:0x0000ff|40.737102,-73.990318|40.749825,-73.987963


https://maps.googleapis.com/maps/api/staticmap?size=400x400&path=color:0x0000ff|40.737102,-73.990318|40.749825,-73.987963|Iowa


https://maps.googleapis.com/maps/api/staticmap?size=400x400&path=color:0x0000ff|40.737102,-73.990318|40.749825,-73.987963|Iowa&path=color:0xff0000|weight:7|Iowa|Minneapolis


## Styled maps

https://developers.google.com/maps/documentation/staticmaps/#StyledMaps


style=feature:road.local|element:labels|visibility:off

https://maps.googleapis.com/maps/api/staticmap?size=400x400&markers=Brighton+Beach,NY&style=feature:landscape|element:geometry|gamma:8.0



## Construct a URL

http://docs.python-requests.org/en/latest/api/#lower-level-classes


~~~py
from requests import Request
req = Request('get', url = 'http://www.example.com', 
                  params = {'hello': 'world'})
preq = req.prepare()
print(preq.url)                  
# http://www.example.com/?hello=world
~~~

~~~py
from requests import Request
p = Request('get', url = 'http://www.example.com', 
                  params = {'hello': 'world',
                            'things': ['a', 'b', 'c']    
                    }).prepare()
print(p.url)                  
# http://www.example.com/?hello=world&things=a&things=b&things=c
~~~



-----------

## Static maps

https://developers.google.com/maps/documentation/streetview/

