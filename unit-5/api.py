import requests
import json
'''
response = requests.get('http://api.open-notify.org/astros.json').json()

# response_data = response.json()
# - JSON keys must have double quotations; values can be anything

# json_convert = json.dumps(response_data, indent=2)
# json_loads = json.loads(response_data)
# Lookup NHL API
# print(response['message'])

for person in response['people']:
    print(person['name'])
'''
'''
response = requests.get('https://statsapi.web.nhl.com/api/v1/teams')
response_data = response.json()
nhl_teams = response_data['teams']
print(json.dumps(nhl_teams[0], indent=2))
# - homework: print venue names of all nhl teams
# - print the number of teams in eastern conference
# - which team is the oldest
'''
#import requests
response = requests.get('https://statsapi.web.nhl.com/api/v1/teams').json()
data = response['teams']

for team in data:
    print(team['venue']['name'])

team_count = 0
for team in data:
    if team['conference']['name'] == 'Eastern':
        # print(team['name'])
        team_count += 1
print('Total No. of Eastern Conference Teams: ' + str(team_count))

result = []
for team in data:
    result.append(
        {'name': team['name'], 'firstYearOfPlay': team['firstYearOfPlay']})
    i += 1
newlist = sorted(result, key=lambda k: k['firstYearOfPlay'])
print(newlist[0])
