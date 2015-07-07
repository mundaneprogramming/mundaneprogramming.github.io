import flickrapi
from os import environ
flickr = flickrapi.FlickrAPI(environ['FLICKR_KEY'], environ['FLICKR_SECRET'])

# Upload API
# https://www.flickr.com/services/api/upload.api.html
# http://stuvel.eu/media/flickrapi-docs/documentation/4-uploading.html


flickr.upload("/tmp/gliders.jpg",
    title = "hello",
    description = "lorem ipsum jkasldfjklsjdfklasjdf",
    tags = "you there are fun",
    format = 'rest'
)
