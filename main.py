import iGetMusic as iGet
import random

PATH_TO_DATASET = "./dataset/rym_top_5000_all_time.csv"


def get_image(songName: str) -> str:
    """Returns album's cover using iGetMusic with search query of title and artist."""
    song = iGet.get(term=songName, country="US", explicit=True)
    image_url = song[0].getImage()
    image_url = iGet.resizeImage(image_url, 1000)
    return image_url


def get_title_from_index(index, dataset_path=PATH_TO_DATASET):
    """Returns formatted title of an album from an index of the dataset."""
    file = open(dataset_path, "r", encoding="UTF-8")
    for i, line in enumerate(file):
        if i == index:
            return line
        elif i > index:
            break
    file.close()

    return str()


def get_random_title() -> str:
    """Returns album's info. Uses get_title_from_index."""
    index = random.randint(1, 5000)
    _, album_title, album_artist, *_ = get_title_from_index(index).split(",")
    return f"{album_title} {album_artist}"


def get_random_titles() -> list:
    """Finds two unique albums and returns a list of formatted outputs. Uses get_title_from_index."""
    output_list = list()
    index1 = random.randint(1, 5000)
    index2 = random.randint(1, 5000)

    while index1 == index2:
        index2 = random.randint(1, 5000)

    _, album_title1, album_artist1, *_ = get_title_from_index(index1).split(",")
    _, album_title2, album_artist2, *_ = get_title_from_index(index2).split(",")

    output_list.append(f"{album_title1} {album_artist1}")
    output_list.append(f"{album_title2} {album_artist2}")

    return output_list


inital_albums = get_random_titles()
album_1_info = inital_albums[0]
album_2_info = inital_albums[1]
album_1_photo = None
album_2_photo = None

while album_1_photo == None or album_2_photo == None:
    try:
        album_1_photo = get_image(inital_albums[0])
        album_2_photo = get_image(inital_albums[1])
    except Exception as e:
        print(f"Error retrieving image: {e}")
        inital_albums = get_random_titles()
        album_1_info = inital_albums[0]
        album_2_info = inital_albums[1]

print(inital_albums[0])
print(inital_albums[1])
print(album_1_photo)
print(album_2_photo)
