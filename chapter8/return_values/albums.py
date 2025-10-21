def make_album(artist, album, number_of_songs=""):
    """This functions makes an artist's album clearly visible to him"""
    if number_of_songs:
        music = {'artist': artist, 'album': album, 'Number of songs on album': number_of_songs}
        return music
    
    else:
        music = {'artist': artist, 'album': album}
        return music




musician = make_album('sombr', 'Half past 12')
print(musician)

musician = make_album('Ed Sheeran', 'Plus')
print(musician)

musician = make_album('Linkeon', 'Nirvana')
print(musician)

#number of songs with the dictionary
musician = make_album('Abba', 'Lost in the wind', '13')
print(musician)