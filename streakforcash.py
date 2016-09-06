# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 14:35:23 2015

@author: rmallya1
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import DataFrame
import datetime

def main():
    
    
    dt = datetime.date(2013,05,01)
    while str(dt) != '2015-09-05':
        dt = dt + datetime.timedelta(days=1)
        dts = str(dt)
        dts = dts.replace('-','')
        print dts
        r = requests.get("http://streak.espn.go.com/en/entry?date=" + dts)
        data = r.text
        soup = BeautifulSoup(data)
        
        #print soup.prettify()
        
        rows = soup.find_all('div',{"class":"matchup-container"})
        
        #print rows
        for row in rows:
           f = open('C:/RK/sforcash2.txt','a')
           if row.find('div',{"class":"gamequestion"}) == None:
               gameq = row.find('div',{"class":"left"}).text
           else:
               gameq = row.find('div',{"class":"gamequestion"}).text
           start = row.find('td',{"class":"mg-column1 start"}).text
           sport = row.find('td',{"class":"mg-column2 sport"}).text
           opponents = row.find('td',{"class":"mg-column3 opponents  "}).text
           result = row.find('td',{"class":"mg-column4 result  "}).text
           users = row.find('td',{"class":"mg-column6 wpw"}).text
           opponents1 = row.find('td',{"class":"mg-column3 opponents   last"}).text
           result1 = row.find('td',{"class":"mg-column4 result   last"}).text
           str1 = dts + '\t' + gameq + '\t' + start + '\t' + sport + '\t' + opponents + '\t' + result + '\t' + users + '\t' + opponents1 + '\t' + result1 + '\n'
           f.write(str1)
           f.close()
       #df = pd.DataFrame([[start, sport, opponents, result, users, opponents1, result1]])
       #print df
        #print start
    #if f.closed() == False:
    f.close()
    #table_data = parse_rows(rows)
    #print table_data
    
def parse_rows(rows):
    results = []
    for row in rows:
        #table_data = row.find_all('td',{"class":"mg-column6 wpw"})
        game = rows.find('td',{"class":"mg-column1 start"})
        if game:
            results.append([data.get_text().strip() for data in game])


if __name__ == "__main__":
    main()