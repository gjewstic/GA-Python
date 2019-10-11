'''
Dictionary of ten popular songs (a list of dictionaries)
'''

songs = [
    {'title': 'Song 1', 'genre': 'Rock 1', 'artist': 'Artist 1', 'length': 4.70},
    {'title': 'Song 2', 'genre': 'Rock 2', 'artist': 'Artist 9', 'length': 4.71},
    {'title': 'Song 3', 'genre': 'Rock 1', 'artist': 'Artist 3', 'length': 4.72},
    {'title': 'Song 4', 'genre': 'Rock 4', 'artist': 'Artist 9', 'length': 4.73},
    {'title': 'Song 5', 'genre': 'Rock 5', 'artist': 'Artist 1', 'length': 4.74},
    {'title': 'Song 6', 'genre': 'Rock 1', 'artist': 'Artist 6', 'length': 4.75},
    {'title': 'Song 7', 'genre': 'Rock 7', 'artist': 'Artist 1', 'length': 4.76},
    {'title': 'Song 8', 'genre': 'Rock 8', 'artist': 'Artist 8', 'length': 4.77},
    {'title': 'Song 9', 'genre': 'Rock 2', 'artist': 'Artist 1', 'length': 4.78},
    {'title': 'Song 10', 'genre': 'Rock 10', 'artist': 'Artist 10', 'length': 4.79}
]
'''
# Numbers - how do we find the min or max in a list


def find_max(my_list):
    max_value = my_list[0]
    for idx in range(1, len(my_list)):
        if my_list[idx] > max_value:
            max_value = my_list[idx]
    return max_value


num_list = [1, 2, 5, 33, 3, 11, 8, 6, 65, 43, 42, 92]
#largest = find_max(num_list)

#print(largest)
'''


def longest_song(playlist):
    '''
    longest running song in the list
    range(1, len(playlist)) == starting at position 1
    '''
    max_song = {'title': playlist[0]['title'], 'length': playlist[0]['length']}
    for idx in range(1, len(playlist)):
        if playlist[idx]['length'] > max_song['length']:
            max_song['title'] = playlist[idx]['title']
            max_song['length'] = playlist[idx]['length']
    return max_song


# print(longest_song(songs))


def longest_song_alt(playlist):
    '''
    longest running song in the list
    '''
    max_song = {'title': playlist[0]['title'], 'length': playlist[0]['length']}
    for song in playlist:
        if song['length'] > max_song['length']:
            max_song['title'] = song['title']
            max_song['length'] = song['length']
    return max_song


# print(longest_song_alt(songs))


def most_song_artist(any_playlist):
    '''
    Brings back the artist with the most songs in the list
    '''
    artist_counter = {}
    for song in any_playlist:
        if song['artist'] in artist_counter:
            artist_counter[song['artist']] += 1
        else:
            artist_counter[song['artist']] = 1

    return artist_counter


print(most_song_artist(songs))


'''
broken code:
Brings back the artist with the most songs in the list
Trying to deal with the slash (/) in an artist name
def most_song_artist(any_playlist):
    artist_counter = {}
    for song in any_playlist:
        # split the artist name along slash
        artist_names = song['artist'].split('/')
        if len(artist_names):
            if artist_names[0] in artist_counter or artist_names[1] in artist_counter:
                artist_counter[song['artist']] += 1
        else:
            if song['artist'] in artist_counter:
                artist_counter[song['artist']] += 1
            else:
                artist_counter[song['artist']] = 1
    return artist_counter

'''
if any([1, 2, 3, 4, 5, 6, 7]) in [1, 3, 5]:
    print('Yes!!!')

# Data Science - what is my project?  what is my data set?
# kaggle.com - list of open data sets
