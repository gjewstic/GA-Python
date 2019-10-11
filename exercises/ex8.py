import random
destinations = ['Mexico', 'Vancouver', 'Bangkok', 'London',
                'Sydney', 'Brussels', 'Edinburgh', 'Lisbon', 'Venice', 'Zurich']
#rank = random.randint(1, 10)

for idx in range(len(destinations)):
    rank = random.randint(1, 100)
    print(destinations[idx] + ' - ' + str(rank))
