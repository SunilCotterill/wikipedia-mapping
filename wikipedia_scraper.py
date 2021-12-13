import os, sys, argparse, datetime, atexit, urllib.request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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
coordinates = rhs[:20]
print(coordinates)



   