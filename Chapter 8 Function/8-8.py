def make_album(singer,album_name):
    album = {'Singer Name':singer,'Album Name':album_name}
    return album

while True:
    singer_name=input("Please type your favorite singer.")
    name_of_album=input("Please type your album name.")
    if(singer_name == 'quit' or name_of_album == 'quit'):
        break
    print(make_album(singer_name,name_of_album))