import iGetMusic as iGet
import random

PATH_TO_FILE = "./dataset/rym_top_5000_all_time.csv"

def getImage(songName: str) -> str:
    song = iGet.get(term=songName, country="CA", explicit=True)
    imageURL = song[0].getImage()
    imageURL = iGet.resizeImage(imageURL,1000)
    return imageURL


def getTitleFromIndex(index):
    file = open(PATH_TO_FILE,"r",encoding="UTF-8")
    for i, line in enumerate(file):
        if i == index:
            return line
        elif i > index:
            break
    file.close()
    return str()

def getRandomAlbumTitle() -> str:
    index = random.randint(1,5000)
    _, album_title, album_artist, *_ = getTitleFromIndex(index).split(",")
    print(f'randomTitle() returns: {album_title} {album_artist}')
    return f'{album_title} {album_artist}'
        
def getRandomAlbumTitles() -> list:
    outputList = list()
    index1 = random.randint(1,5000)
    index2 = random.randint(1,5000)
    
    while index1 == index2:
        index2 = random.randint(1,5000)

    _, album_title1, album_artist1, *_ = getTitleFromIndex(index1).split(",")
    _, album_title2, album_artist2, *_ = getTitleFromIndex(index2).split(",")

    outputList.append(f'{album_title1} {album_artist1}')
    outputList.append(f'{album_title2} {album_artist2}')
    return outputList

initialAlbums = getRandomAlbumTitles()


album1 = None
album2 = None

while album1 == None or album2 == None:
    try:
        album1 = getImage(initialAlbums[0])
        album2 = getImage(initialAlbums[1])
    except Exception as e:
        print(f'Error retrieving image for {initialAlbums[0]}: {e}')
        initialAlbums = getRandomAlbumTitles()

print(initialAlbums[0])
print(initialAlbums[1])
print(album1)
print(album2)