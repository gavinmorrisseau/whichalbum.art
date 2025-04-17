import iGetMusic as iGet
import random
import json

IMAGE_WIDTH = 1000
PATH_TO_DATASET = "./dataset/rym_top_5000_all_time.csv"

def get_image(query: str) -> str:
    """Returns album's cover using iGetMusic with search query of title and artist."""
    song = iGet.get(term=query, country="US", explicit=True)
    image_url = song[0].getImage()
    image_url = iGet.resizeImage(image_url, IMAGE_WIDTH)
    return image_url

def get_album_from_index(index, dataset_path=PATH_TO_DATASET) -> dict:
    """Returns formatted title of an album from an index of the dataset."""
    file = open(dataset_path, "r", encoding="UTF-8")
    for i, line in enumerate(file):
        if i == index:
            file.close()
            _, title, artist, date, genre, *_ = line.split(",")
            output = dict()
            output['title'] = title
            output['artist'] = artist
            output['date'] = date
            output['genre'] = genre
            return output
        elif i > index:
            break
    return 'Error in: get_title_from_index()!'

def get_random_album(exclude_index=None) -> dict:
    """Returns album's info. Uses get_title_from_index."""
    index = random.randint(1, 5000)
    if exclude_index:
        while index == exclude_index:
            index = random.randint(1, 5000)
    album = get_album_from_index(index)
    return album

def get_random_albums() -> list:
    """Finds two unique albums and returns a list of formatted outputs. Uses get_title_from_index."""
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
        except Exception as e:
            #print(f"Error retrieving image: {e}")
            album1, album2 = get_random_albums()
            album1_photo_link = None
            album2_photo_link = None

    album1['link'] = album1_photo_link
    album2['link'] = album2_photo_link

    return album1, album2

if __name__ == "__main__":
    print(main())
    # Print output is expected for subprocess
