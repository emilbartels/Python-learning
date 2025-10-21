def make_album(artist, album, number_of_songs=""):
    """This functions makes an artist's album clearly visible to him"""
    if number_of_songs:
        music = {'artist': artist, 'album': album, 'Number of songs on album': number_of_songs}
        return music
    
    else:
        music = {'artist': artist, 'album': album}
        return music
    
while True:
    print(f'\nI want to know your favorit artists album:')
    print("enter 'quit' to quit the program")

    artist = input(f'\nEnter the name of your favorite artist:')
    if artist == 'quit':
        break

    album = input(f'\nEnter your favorite album from {artist}:')
    if album == 'quit':
        break

    musican = make_album(artist, album)
    print(musican)