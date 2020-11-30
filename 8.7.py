#8.7 Ablum
#Write a function called make_album() that builds a dictionary
#describing a music album. The function should take in an artist name and an
#album title, and it should return a dictionary containing these two pieces of
#information. Use the function to make three dictionaries representing different
#albums. Print each return value to show that the dictionaries are storing the
#album information correctly.

def make_album(artist, title, tracks=0):
    album_dict = {
        'artist': artist.title(),
        'title' : title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('taylor swift', 'repuation')
print(album)

album = make_album('taylor swift', 'lover',tracks=16)
print(album)

album = make_album('taylor swift', 'red')
print(album)


