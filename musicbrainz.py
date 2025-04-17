import musicbrainzngs as mb
mb.set_useragent("whichalbum.art", "0.1", "https://github.com/gavinmorrisseau/whichalbum.art")
result = mb.search_release_groups("london calling the clash", limit=1, type='album')
print(result)
MBID = result['release-group-list'][0]['release-list'][0]['id']
print(MBID)
image_list = mb.get_image_list(MBID)
image_URL = image_list['images'][0]['image']
print(image_URL)