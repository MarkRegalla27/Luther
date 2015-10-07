import requests
import pandas as pd

from bs4 import BeautifulSoup
import dateutil.parser
import pickle
from datetime import datetime

url2015List = ['http://www.boxofficemojo.com/yearly/chart/?page=1&view=releasedate&view2=domestic&yr=2015&p=.htm',
'http://www.boxofficemojo.com/yearly/chart/?page=2&view=releasedate&view2=domestic&yr=2015&p=.htm',
'http://www.boxofficemojo.com/yearly/chart/?page=3&view=releasedate&view2=domestic&yr=2015&p=.htm',
'http://www.boxofficemojo.com/yearly/chart/?page=4&view=releasedate&view2=domestic&yr=2015&p=.htm',
'http://www.boxofficemojo.com/yearly/chart/?page=5&view=releasedate&view2=domestic&yr=2015&p=.htm']

url2014List = ['http://www.boxofficemojo.com/yearly/chart/?page=1&view=releasedate&view2=domestic&yr=2014&p=.htm', 
                'http://www.boxofficemojo.com/yearly/chart/?page=2&view=releasedate&view2=domestic&yr=2014&p=.htm',
                'http://www.boxofficemojo.com/yearly/chart/?page=3&view=releasedate&view2=domestic&yr=2014&p=.htm',
                'http://www.boxofficemojo.com/yearly/chart/?page=4&view=releasedate&view2=domestic&yr=2014&p=.htm',
                'http://www.boxofficemojo.com/yearly/chart/?page=5&view=releasedate&view2=domestic&yr=2014&p=.htm',
                'http://www.boxofficemojo.com/yearly/chart/?page=6&view=releasedate&view2=domestic&yr=2014&p=.htm',
                'http://www.boxofficemojo.com/yearly/chart/?page=7&view=releasedate&view2=domestic&yr=2014&p=.htm',
                'http://www.boxofficemojo.com/yearly/chart/?page=8&view=releasedate&view2=domestic&yr=2014&p=.htm']

url2013List = ['http://www.boxofficemojo.com/yearly/chart/?page=1&view=releasedate&view2=domestic&yr=2013&p=.htm',
                'http://www.boxofficemojo.com/yearly/chart/?page=2&view=releasedate&view2=domestic&yr=2013&p=.htm',
                'http://www.boxofficemojo.com/yearly/chart/?page=3&view=releasedate&view2=domestic&yr=2013&p=.htm',
                'http://www.boxofficemojo.com/yearly/chart/?page=4&view=releasedate&view2=domestic&yr=2013&p=.htm',
                'http://www.boxofficemojo.com/yearly/chart/?page=5&view=releasedate&view2=domestic&yr=2013&p=.htm',
                'http://www.boxofficemojo.com/yearly/chart/?page=6&view=releasedate&view2=domestic&yr=2013&p=.htm',
                'http://www.boxofficemojo.com/yearly/chart/?page=7&view=releasedate&view2=domestic&yr=2013&p=.htm']

url2012List = ['http://www.boxofficemojo.com/yearly/chart/?page=1&view=releasedate&view2=domestic&yr=2012&p=.htm',
                'http://www.boxofficemojo.com/yearly/chart/?page=2&view=releasedate&view2=domestic&yr=2012&p=.htm',
                'http://www.boxofficemojo.com/yearly/chart/?page=3&view=releasedate&view2=domestic&yr=2012&p=.htm',
                'http://www.boxofficemojo.com/yearly/chart/?page=4&view=releasedate&view2=domestic&yr=2012&p=.htm',
                'http://www.boxofficemojo.com/yearly/chart/?page=5&view=releasedate&view2=domestic&yr=2012&p=.htm',
                'http://www.boxofficemojo.com/yearly/chart/?page=6&view=releasedate&view2=domestic&yr=2012&p=.htm',
                'http://www.boxofficemojo.com/yearly/chart/?page=7&view=releasedate&view2=domestic&yr=2012&p=.htm']

yearList = [2015, 2014, 2013, 2012]
urlList = [url2015List, url2014List, url2013List, url2012List]
rowforindex = ['Rank', 'Title', 'Studio', 'Total Gross', 'Total Theaters', 'Opening Gross',
               'Opening Theaters', 'Opening Date', 'Closing Date', 'Year']
totalFrame = pd.DataFrame()

j = 0
for i in urlList:
    for k in i:
        holderFrame = pd.read_html(k)
        holderFrame = holderFrame[5]
        holderFrame = holderFrame.drop(holderFrame.index[0:2])
        holderFrame = holderFrame.drop(holderFrame.index[-4:])
        holderFrame['year'] = yearList[j]
        totalFrame = totalFrame.append(holderFrame, ignore_index=True)
    j += 1

totalFrame.columns = rowforindex
totalFrame = totalFrame.dropna()

#Strip $ signs from money amounts and convert them to floats
totalFrame['Opening Gross'] = totalFrame['Opening Gross'].map(lambda x: x.strip('$'))
totalFrame['Total Gross'] = totalFrame['Total Gross'].map(lambda x: x.strip('$'))
totalFrame['Opening Gross'] = totalFrame['Opening Gross'].map(lambda x: x.replace(',',''))
totalFrame['Total Gross'] = totalFrame['Total Gross'].map(lambda x: x.replace(',',''))
totalFrame['Opening Gross'] = totalFrame['Opening Gross'].map(lambda x: float(x))
totalFrame['Total Gross'] = totalFrame['Total Gross'].map(lambda x: float(x))

#Convert number of theaters to floats
totalFrame['Total Theaters'] = totalFrame['Total Theaters'].map(lambda x: float(x))
totalFrame['Opening Theaters'] = totalFrame['Opening Theaters'].map(lambda x: float(x))

#Attempt to convert date from unicode to datetime.  Not working as of 10-1-15
#df['Opening Date'] = df['Opening Date'].map(lambda x: datetime.strptime(x,'%m/%d'))

with open('totalFrame.pkl', 'w') as picklefile:
    pickle.dump(totalFrame, picklefile)
