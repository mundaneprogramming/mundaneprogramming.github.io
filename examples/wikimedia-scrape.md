---
title: Extract Wikimedia image stuff
related_links:
  - title: MediaWiki Commons API documentation
    url: https://commons.wikimedia.org/wiki/Commons:API/MediaWiki
---


To get image info:

https://commons.wikimedia.org/w/api.php?action=query&prop=imageinfo&titles=Image:Nellie_Bly-Mad-House-07.png

To get metadata

https://commons.wikimedia.org/w/api.php?action=query&prop=imageinfo&iiprop=metadata&iimetadataversion=latest&titles=Image:Nellie_Bly-Mad-House-07.png

To get even more stuff, including licenses:

https://commons.wikimedia.org/w/api.php?action=query&prop=imageinfo&iiprop=extmetadata&titles=Image:Nellie_Bly-Mad-House-07.png
