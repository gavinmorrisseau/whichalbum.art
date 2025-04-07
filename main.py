import iGetMusic as iGet
import random

PATH_TO_FILE = "./dataset/rym_top_5000_all_time.csv"

def getImage(songName: str) -> str:
    song = iGet.get(term=songName, country="CA", explicit=True)
    imageURL = song[0].getImage()
    imageURL = iGet.resizeImage(imageURL,1000)
    return imageURL

def randomTitle() -> str:
    index = random.randint(1,5000)
    file = open(PATH_TO_FILE,"r",encoding="UTF-8")
    for i, line in enumerate(file):
        if i == index:
            _, album_title, album_artist, *_ = line.split(",")
        elif i > index:
            break
    print(f'randomTitle() returns: {album_title} {album_artist}')
    return f'{album_title} {album_artist}'\
        
print(getImage(randomTitle()))
