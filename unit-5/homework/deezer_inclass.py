import requests
import json
url = "https://deezerdevs-deezer.p.rapidapi.com/search"
querystring = {"q": "eminem"}
headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "0bddc33020msh443a1cf18b3644cp1ef6cejsn179c39f77c2e"
}
response = requests.request("GET", url, headers=headers, params=querystring)
# print(response.json()['data'][0].keys())
eminem_tracks = response.json()['data']
print(len(eminem_tracks))

album_count = {}
total = 0

for track in eminem_tracks:
    album_title = track['album']['title']
    album_count[album_title] = 'present'
print(len(album_count))


def unique_disc(list):
    unique_list = []
    for disc in list:
        if disc not in unique_list:
            unique_list.append(disc)

    return unique_list


x = []

for disc in eminem_tracks:
    x.append(disc['album']['title'])

print(unique_disc(x))
