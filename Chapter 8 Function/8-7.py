def make_album(singer,album_name):
    album = {'Singer Name':singer,'Album Name':album_name}
    return album
sam_smith = make_album('Sam Smith',"I'm Not the Only One")
print(sam_smith)