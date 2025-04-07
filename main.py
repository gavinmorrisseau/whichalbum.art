import iGetMusic as iGet

def getImage(str: songName) -> str:
    song = iGet.get(term=songName, country="CA", explicit=True)
    imageURL = song[0].getImage()
    imageURL = iGet.resizeImage(image,1000)
    return imageURL

print(getImage(''))



