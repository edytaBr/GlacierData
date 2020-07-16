#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 10:28:34 2020

@author: edyta
"""
import pandas as pd
from bs4 import BeautifulSoup
import requests

url="http://glacier.nve.no/Glacier/viewer/CI/en/nve/ClimateIndicatorInfo/257?name=Sydbreen"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")

text1 =[]
for link in soup.find_all("table", attrs={"class": "table table-bordered", "id": "lengthTable"}):
   text1.append("Inner Text: {}".format(link.text)) 

a = []
for elem in text1:
    a.append(elem.split("\n"))
 
    
data = a[0]

year = data[2::5]
length = data[3::5]
mass = data[4::5]


glacier_data = pd.DataFrame(list(zip(year, length, mass)), columns =['Year', 'Length', 'Mass'])