import numpy as np
import requests
website_url = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').text
from bs4 import BeautifulSoup
soup = BeautifulSoup(website_url,'lxml')
print(soup.prettify())

My_table = soup.find('table',{'class':'wikitable sortable'})
My_table

print(My_table.tr.text)
headers="Postcode,Borough,Neighbourhood"

table1=""
for tr in My_table.find_all('tr'):
        row1=""
            for tds in tr.find_all('td'):
                        row1=row1+","+tds.text
                            table1=table1+row1[1:]
                            print(table1)

file=open("toronto.csv","wb")
#file.write(bytes(headers,encoding="ascii",errors="ignore"))
file.write(bytes(table1,encoding="ascii",errors="ignore"))

import pandas as pd
df = pd.read_csv('toronto.csv',header=None)
df.columns=["Postalcode","Borough","Neighbourhood"]
df.head(10)
indexNames = df[ df['Borough'] =='Not assigned'].index

# Delete these row indexes from dataFrame
df.drop(indexNames , inplace=True)
dh.head(10)
df.loc[df['Neighbourhood'] =='Not assigned' , 'Neighbourhood'] = df['Borough']
df.head(10)
result = df.groupby(['Postalcode','Borough'], sort=False).agg( ', '.join)
    df_new=result.reset_index()
    df_new.head(15)
df_new.shape

