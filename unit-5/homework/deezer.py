import requests
import json
import random

eminem = requests.get(
    'https://api.deezer.com/artist/13').json()  # - Dictionary
eminem_albums = requests.get(
    'https://api.deezer.com/artist/13/albums').json()  # - Dictionary

# print(type(eminem))
# print(type(eminem_albums))
# print(eminem_albums['data'])
# Tracks: https://api.deezer.com/album/302127/tracks

# print(eminem)
json_convert_eminem = json.dumps(eminem, indent=2)
json_convert_eminem_albums = json.dumps(eminem_albums, indent=2)

# print(json_convert_eminem)
# print(json_convert_eminem_albums)

eminem_album_list = []
eminem_track_list = []
eminem_exp_lyrics_count = 0
eminem_total_track_count = 0

for eminem_album in eminem_albums['data']:
    # print(eminem_album['title'])
    # Generate the URI for each track
    eminem_uri = 'https://api.deezer.com/album/' + \
        str(eminem_album['id']) + '/tracks'
    eminem_tracks = requests.get(eminem_uri).json()
    for eminem_track in eminem_tracks['data']:
        # print(json.dumps(eminem_track, indent=2))
        # - Building the playlist
        track_dict = {'id': eminem_track['id'],
                      'album_title': eminem_album['title'],
                      'readable': eminem_track['readable'],
                      'title': eminem_track['title'],
                      'title_short': eminem_track['title_short'],
                      # 'title_version': eminem_track['title_version'],
                      'link': eminem_track['link'],
                      'duration': eminem_track['duration'],
                      'rank': eminem_track['rank'],
                      'explicit_lyrics': eminem_track['explicit_lyrics'],
                      'explicit_content_lyrics': eminem_track['explicit_content_lyrics']}
        eminem_track_list.append(track_dict)

        # - Generate the number of tracks for artist Eminem
        eminem_total_track_count += 1

        # - Generate a count of all tracks containing explicit lyrics
        if eminem_track['explicit_lyrics'] == True:
            eminem_exp_lyrics_count += 1

    # print(json.dumps(eminem_tracks, indent=2))

'''
def unique_disc(list):
    unique_list = []
    for disc in list:
        if disc not in unique_list:
            unique_list.append(disc)
    for disc in unique_list:
        print(disc)

unique_disc(eminem_album_list)
'''

for disc in eminem_albums['data']:
    disc_dict = {'Title': disc['title'],
                 'Album_Release_Date': disc['release_date']}
    eminem_album_list.append(disc_dict)

'''
for dictionary in eminem_album_list:
    print(dictionary['Title'])

print(eminem_album_list)
'''

print(f'Total Number of Eminem Tracks: {eminem_total_track_count}')
# print('Total Number of Eminem Tracks: {}'.format(eminem_total_track_count))

print(
    f'Total Number of Eminem Tracks (Explicit Lyrics): {eminem_exp_lyrics_count}')
# print('Total Number of Eminem Tracks (Explicit Lyrics): {}'.format(eminem_exp_lyrics_count))

print(f'Total Number of Eminem Albums: {len(eminem_album_list)}')
# print('Total Number of Eminem Albums: {}'.format(len(eminem_album_list)))

# print('Aftermath' in eminem_album_list)
aftermath = 'Aftermath' in eminem_album_list
if aftermath == True:
    print('Aftermath is in the Deezer Catalogue')
else:
    print('Aftermath is NOT in the Deezer Catalogue')

# print(eminem_track_list[:10])
playlist_count = 1
while playlist_count <= 10:
    random_track = random.randint(0, len(eminem_track_list))

    print('Track No. {}: {}, Album:'.format(
        playlist_count, eminem_track_list[random_track]['title']), eminem_track_list[random_track]['album_title'])
    playlist_count += 1

'''
eminem = requests.get('https://api.deezer.com/search?q=eminem').json()
cardi_b = requests.get('https://api.deezer.com/search?q=cardi%20b').json()
ed_sheeran = requests.get(
    'https://api.deezer.com/search?q=Ed%20Sheeran').json()

json_convert = json.dumps(eminem, indent=2)

# print(json_convert)
# Track Data

# Data/explicit_lyrics (bool)
# Data/artist/name
# Data/album/title

eminem_data = eminem['data']
cardi_b_data = cardi_b['data']
ed_sheeran_data = ed_sheeran['data']

exp_eminem = 0

for track in eminem_data:
    if track['explicit_lyrics'] == True:
        exp_eminem += 1

print(f'Total Eminem Tracks: {len(eminem_data)}')
print(f'Total Cardi B Tracks: {len(cardi_b_data)}')
print(f'Total Ed Sheeran Tracks: {len(ed_sheeran_data)}')

exp_cardi_b = 0

for track in cardi_b_data:
    if track['explicit_lyrics'] == True:
        exp_cardi_b += 1

exp_ed_sheeran = 0

for track in ed_sheeran_data:
    if track['explicit_lyrics'] == True:
        exp_ed_sheeran += 1

print(f'Total Explicit Eminem: {exp_eminem}')
print(f'Total Explicit Cardi B: {exp_cardi_b}')
print(f'Total Explicit Ed Sheeran: {exp_ed_sheeran}')

# Python program to check if two
# to get unique values from list
# using traversal

# function to get unique values


for disc in eminem_data:
    print(disc['album']['title'])

def unique_disc(list):
    unique_list = []
    for disc in list:
        if disc not in unique_list:
            unique_list.append(disc)
    
    return unique_list

x = []

for disc in eminem_data:
    x.append(disc['album']['title'])

print(unique_disc(x))
'''
