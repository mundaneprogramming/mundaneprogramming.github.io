---
title: Geocode a Photo
related_links:
  - title: "erans Gist: Get Latitude and Longitude from EXIF using PIL"
    url: https://gist.github.com/erans/983821

---



~~~py
import exifread
f = open("/tmp/photo.jpg", "rb")
exif = exifread.process_file(f)
exif['GPS GPSLatitude']
#  (0x0002) Ratio=[41, 53, 569/20] @ 1826
z = exif['GPS GPSLatitude']
type(z)
#  exifread.classes.IfdTag
z.values
# [41, 53, 569/20]
~~~

## Converting latitude and longitude

~~~py
def convert_to_degrees(values):
    """values is a list that looks like: [41, 53, 569/20] 
       and each thing is a  exifread.utils.Ratio"""
    degrees, mins, secs = [v.num / v.den for v in values]
    return degrees + (mins / 60.0) + (secs / 3600.0)
~~~
