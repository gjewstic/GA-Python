'''
car_details = {'make': 'Chevy', 'model': 'Corvette',
               'year': '1963', 'seats': 2, 'color': 'Black'}
person = {'height': 1.80, 'weight': 180, 'eye_color': 'brown',
          'hair_color': 'black', 'name': 'John'}
eng_to_pl = {'yes': 'tak', 'no': 'nie', 'dad': 'tata'}
office_supplies_brands = {'stapler': 'Staples',
                          'calculator': 'Casio', 'computer': 'Dell'}
color_descriptions = {'orange': 'bright', 'blue': 'dark', 'red': 'deep'}

# print(car_details)

# get a specific value from the dictionary
# print(car_details['make'])

# iterate over a dictionary
# for key in car_details:
#    print(key)

# for value in car_details:
#    print(car_details[value])

# iterate through dictionary
for key in car_details:
    print(key, car_details[key])

# Search a dictionary: check if key is in a dictionary
# if 'year' in car_details:
#    print(car_details['year'])

# if a key is not in the dictionary
# print(eng_to_pl['mom'])
'''
'''
homework:

Build a list of dictionaries of all major cities in Canada
each dictionary will store the following:
- name
- latitude
- longitude
- size
- population

All dictionaries go into a list
'''
'''
# Canadian Cities
toronto = {
    'name': 'Toronto',
    'pop': 3000000,
    'long': '79, 24',
    'lat': '43, 40',
    'size': 630
}
montreal = {
    'name': 'Montreal',
    'pop': 2500000,
    'long': '80, 26',
    'lat': '44, 41',
    'size': 610
}
vancouver = {
    'name': 'Vancouver',
    'pop': 2800000,
    'long': '25, 27',
    'lat': '46, 42',
    'size': 590
}
edmonton = {
    'name': 'Edmonton',
    'pop': 700000,
    'long': '31, 30',
    'lat': '29, 27',
    'size': 475
}
calgary = {
    'name': 'Calgary',
    'pop': 1500000,
    'long': '31, 28',
    'lat': '29, 26',
    'size': 440
}
victoria = {
    'name': 'Victoria',
    'pop': 800000,
    'long': '21, 22',
    'lat': '29, 19',
    'size': 452
}
regina = {
    'name': 'Regina',
    'pop': 450000,
    'long': '27, 25',
    'lat': '26, 21',
    'size': 390
}
winnipeg = {
    'name': 'Winnipeg',
    'pop': 750000,
    'long': '37, 34',
    'lat': '31, 27',
    'size': 395
}
ottawa = {
    'name': 'Ottawa',
    'pop': 1000000,
    'long': '40, 42',
    'lat': '29, 17',
    'size': 456
}
quebec_city = {
    'name': 'Quebec City',
    'pop': 700000,
    'long': '44, 41',
    'lat': '44, 29',
    'size': 412
}
halifax = {
    'name': 'Halifax',
    'pop': 600000,
    'long': '52, 49',
    'lat': '31, 29',
    'size': 312
}
charlottetown = {
    'name': 'Charlottetown',
    'pop': 350000,
    'long': '54, 47',
    'lat': '42, 41',
    'size': 190
}
saint_john = {
    'name': 'Saint John',
    'pop': 550000,
    'long': '55, 50',
    'lat': '43, 49',
    'size': 212
}
st_johns = {
    'name': 'St Johns',
    'pop': 400000,
    'long': '55, 52',
    'lat': '43, 48',
    'size': 179
}

canadian_cities = []
canadian_cities.append(toronto)
canadian_cities.append(montreal)
canadian_cities.append(vancouver)
canadian_cities.append(edmonton)
canadian_cities.append(calgary)
canadian_cities.append(regina)
canadian_cities.append(victoria)
canadian_cities.append(winnipeg)
canadian_cities.append(ottawa)
canadian_cities.append(quebec_city)
canadian_cities.append(halifax)
canadian_cities.append(saint_john)
canadian_cities.append(charlottetown)
canadian_cities.append(st_johns)

for i in canadian_cities:
    print(i)

for i in canadian_cities:
    print(i['name'])

for i in canadian_cities:
    print(i['name'], i['pop'])
'''

cities = [
    {
        'name': 'Toronto',
        'pop': 3000000,
        'long': '79, 24',
        'lat': '43, 40',
        'size': 630
    },
    {
        'name': 'Montreal',
        'pop': 2500000,
        'long': '80, 26',
        'lat': '44, 41',
        'size': 610
    },
    {
        'name': 'Vancouver',
        'pop': 2800000,
        'long': '25, 27',
        'lat': '46, 42',
        'size': 590
    },
    {
        'name': 'Edmonton',
        'pop': 700000,
        'long': '31, 30',
        'lat': '29, 27',
        'size': 475
    },
    {
        'name': 'Calgary',
        'pop': 1500000,
        'long': '31, 28',
        'lat': '29, 26',
        'size': 440
    },
    {
        'name': 'Victoria',
        'pop': 800000,
        'long': '21, 22',
        'lat': '29, 19',
        'size': 452
    },
    {
        'name': 'Regina',
        'pop': 450000,
        'long': '27, 25',
        'lat': '26, 21',
        'size': 390
    },
    {
        'name': 'Winnipeg',
        'pop': 750000,
        'long': '37, 34',
        'lat': '31, 27',
        'size': 395
    },
    {
        'name': 'Ottawa',
        'pop': 1000000,
        'long': '40, 42',
        'lat': '29, 17',
        'size': 456
    },
    {
        'name': 'Quebec City',
        'pop': 700000,
        'long': '44, 41',
        'lat': '44, 29',
        'size': 412
    },
    {
        'name': 'Halifax',
        'pop': 600000,
        'long': '52, 49',
        'lat': '31, 29',
        'size': 312
    },
    {
        'name': 'Charlottetown',
        'pop': 350000,
        'long': '54, 47',
        'lat': '42, 41',
        'size': 190
    },
    {
        'name': 'Saint John',
        'pop': 550000,
        'long': '55, 50',
        'lat': '43, 49',
        'size': 212
    },
    {
        'name': 'St Johns',
        'pop': 400000,
        'long': '55, 52',
        'lat': '43, 48',
        'size': 179
    }
]

for i in cities:
    print(i['name'])
'''
dictionary_sample = {
    'age': (4 * 2)
}

print(dictionary_sample)
'''
'''
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
'''
