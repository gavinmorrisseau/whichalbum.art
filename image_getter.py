import random
import musicbrainzngs as mb
VERSION = "0.1"
mb.set_useragent("whichalbum.art", VERSION, "https://github.com/gavinmorrisseau/whichalbum.art")
PATH_TO_DATASET = "./files/rym_top_5000_all_time.csv"
IMAGE_WIDTH = 600

def get_image(query: str) -> str:
    """ Returns an album cover's URL using musicbrainzng's API with search query of title and artist. """
    # Does not account for HTTP 503 declined requests from Musicbrainz
    result = mb.search_release_groups(query, limit=1, type='album')
    # Music Brainz ID for the query album
    MBID = result['release-group-list'][0]['release-list'][0]['id']
    image_list = mb.get_image_list(MBID)
    image_URL = image_list['images'][0]['image']
    return image_URL

def get_album_from_index(index, dataset_path=PATH_TO_DATASET) -> dict:
    """ Returns formatted title of an album from an index of the dataset. """
    output = dict()
    file = open(dataset_path, "r", encoding="UTF-8")
    for i, line in enumerate(file):
        if i == index:
            _, title, artist, date, genre, *_ = line.split(",")
            output['title'] = title
            output['artist'] = artist
            output['date'] = date
            output['genre'] = genre.replace("\"","")
        elif i > index:
            break
    file.close()
    return output

def get_random_album(exclude_index=None) -> dict:
    """ Returns album's info. Uses get_title_from_index. """
    index = random.randint(1, 5000)
    if exclude_index:
        while index == exclude_index:
            index = random.randint(1, 5000)
    album = get_album_from_index(index)
    return album

def get_random_albums() -> list:
    """ Finds two unique albums and returns a list of formatted outputs. Uses get_title_from_index. """
    output_list = list()
    index1 = random.randint(1, 5000)
    index2 = random.randint(1, 5000)
    while index1 == index2:
        index2 = random.randint(1, 5000)
    album1 = get_album_from_index(index1)
    album2 = get_album_from_index(index2)
    output_list.append(album1)
    output_list.append(album2)
    return output_list

def main():
    album1, album2 = get_random_albums()
    album1_photo_link = None
    album2_photo_link = None

    while album1_photo_link is None or album2_photo_link is None:
        try:
            album1_photo_link = get_image(f'{album1['title']} {album1['artist']}')
            album2_photo_link = get_image(f'{album2['title']} {album2['artist']}')
        except Exception:
            album1, album2 = get_random_albums()
            album1_photo_link = None
            album2_photo_link = None

    album1['link'] = album1_photo_link
    album2['link'] = album2_photo_link

    return album1, album2

if __name__ == "__main__":
    # Print output is expected for subprocess
    print(main())
