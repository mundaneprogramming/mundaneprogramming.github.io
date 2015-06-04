---
layout: example
title: Get coordinate data from Google Geocoding
description: |
  Get latitude and longitude, and other Google geodata, for any given location.
featured: true
rank: 1
files:
  - name: code/google-geocode-address.py
    description: CLI google geocode an address plz
---


### Some Google stuff

[Documentation](https://developers.google.com/maps/documentation/geocoding/)

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nisi quia rerum eveniet voluptatem sapiente iste saepe debitis obcaecati, eaque. Aliquam a id nostrum deleniti voluptate maxime perferendis, dolores, sunt voluptas.


#### Example response

[https://maps.googleapis.com/maps/api/geocode/json?address=100+Broadway+New+York,NY](https://maps.googleapis.com/maps/api/geocode/json?address=100+Broadway+New+York,NY)

~~~json

{
   "results" : [
      {
         "address_components" : [
            {
               "long_name" : "100",
               "short_name" : "100",
               "types" : [ "street_number" ]
            },
            {
               "long_name" : "Broadway",
               "short_name" : "Broadway",
               "types" : [ "route" ]
            },
            {
               "long_name" : "Lower Manhattan",
               "short_name" : "Lower Manhattan",
               "types" : [ "neighborhood", "political" ]
            },
            {
               "long_name" : "Manhattan",
               "short_name" : "Manhattan",
               "types" : [ "sublocality_level_1", "sublocality", "political" ]
            },
            {
               "long_name" : "New York",
               "short_name" : "NY",
               "types" : [ "locality", "political" ]
            },
            {
               "long_name" : "New York County",
               "short_name" : "New York County",
               "types" : [ "administrative_area_level_2", "political" ]
            },
            {
               "long_name" : "New York",
               "short_name" : "NY",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "United States",
               "short_name" : "US",
               "types" : [ "country", "political" ]
            },
            {
               "long_name" : "10006",
               "short_name" : "10006",
               "types" : [ "postal_code" ]
            }
         ],
         "formatted_address" : "100 Broadway, New York, NY 10006, USA",
         "geometry" : {
            "location" : {
               "lat" : 40.70791579999999,
               "lng" : -74.01107309999999
            },
            "location_type" : "ROOFTOP",
            "viewport" : {
               "northeast" : {
                  "lat" : 40.70926478029149,
                  "lng" : -74.00972411970849
               },
               "southwest" : {
                  "lat" : 40.7065668197085,
                  "lng" : -74.0124220802915
               }
            }
         },
         "place_id" : "ChIJywL_PBdawokR4bOmKjJY3QE",
         "types" : [ "street_address" ]
      }
   ],
   "status" : "OK"
}
~~~

