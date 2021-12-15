import os, sys, argparse, datetime, atexit, urllib.request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
from bs4 import BeautifulSoup
from urllib.request import urlopen

#url = 'https://en.wikipedia.org/wiki/Special:RandomRootpage'
url =  'https://en.wikipedia.org/wiki/Brassfield_Baptist_Church'

page_html = urlopen(url)

page_soup = BeautifulSoup(page_html, 'html.parser')

tables = page_soup.find_all(id='coordinates')
refs = tables[0].find_all('a', {'class': 'external text'})
link = refs[0].attrs.get('href')
lhs,rhs = link.split('params=')

#this won't work because they don't always have 19 chars
coordinates = rhs[:20]
print(coordinates)


def coordinateToNum(coordinate):
    coordinate1 = coordinate[:10].replace('_','.',1).replace('_','')
    coordinate2 = coordinate[10:].replace('_','.',1).replace('_','')
    if 'N' in coordinate1:
        coordinate1 = float(coordinate1.replace('N', ''))
    else:
        coordinate1 = -1*float(coordinate1.replace('S', '')) 

    if 'E' in coordinate2:
        coordinate2 = float(coordinate2.replace('E', ''))
    else:
        coordinate2 = -1*float(coordinate2.replace('W', '')) 

    
    print(coordinate1)
    print(coordinate2)
    return coordinate1, coordinate2


numCoor1, numCoor2 = coordinateToNum(coordinates)

plt.scatter(x=numCoor1, y=numCoor2)
plt.show()




   