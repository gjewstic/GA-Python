import requests as req
import json

import pandas as pd

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timezone
'''
print(date.date(2019, 9, 22))
print(date.strpdate('2018-09-22', '%A' +
                    ', ' + '%B' + ' ' + '%d' + ', ' + '%Y'))
                    '''
# pandas.io.json.json_normalize()

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=AAPL&outputsize=full&apikey=O39ZFFT346LYU3MI'
response = req.get(url).json()
output = pd.DataFrame(response['Time Series (Daily)']).transpose()
# print(response['Time Series (Daily)'])
# print(type(output))
print(output.dtypes)
'''
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=AAPL&outputsize=full&apikey=O39ZFFT346LYU3MI'
response = req.get(url).json()

print(json.dumps(response, indent=2))
'''
stock_dict = response['Time Series (Daily)']
'''
# print(json.dumps(stock_dict, indent=2))
for i in stock_dict:
    print("%(8. split coefficient)s" % stock_dict[i])
    # print(type("%(8. split coefficient)s" % stock_dict[i]))
print(stock_dict['1999-11-19'])



'''
print(date.today().strftime('%A' + ', ' + '%B' + ' ' + '%d' + ', ' + '%Y'))
print(datetime.today().strftime('%A' + ', ' + '%B' + ' ' + '%d' +
                                ', ' + '%Y' + ' ' + '%H' + ':' + '%M' + ':' + '%S' + ' ' + '%p'))
coursIndice = []
listInd = []
for elt in response['Time Series (Daily)'].keys():
    listInd.append(elt)
listInd.sort(reverse=True)
for e in listInd:
    coursIndice.append(float(response['Time Series (Daily)'][e]['4. close']))

lenIndice = len(coursIndice)
# print(coursIndice)

rentabIndice = []
for j in range(lenIndice-1):
    rentabIndice.append(100*(coursIndice[j+1]/coursIndice[j] - 1))

moyenneMarche = sum(rentabIndice)/len(rentabIndice)
# print(moyenneMarche)
