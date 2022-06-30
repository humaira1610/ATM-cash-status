# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 13:32:53 2022

@author: User
"""
import pandas as pd
import folium
# import folium.plugins as plugins
# import matplotlib.pyplot as plt
from folium.plugins import HeatMap
import numpy as np

data = pd.read_excel('BRAC Bank branches_v3.xlsx')
print(data)

points = [data['Latitude'], data['Longitude'], data['Amount']]
points = np.array(points).T.tolist()

#rescaling gradients #-formula: (val-minVal)/(maxVal-minVal)
mapPoints=[[x[0],x[1],(x[2]-0)/(6000000-0)] for x in points]

gradient = {0.0:'red',
            0.6: 'yellow',
            0.7: 'lime',
            0.8: 'cyan',
            1.0: 'blue'}

m=folium.Map([24.2235923,90.4089993])
HeatMap(mapPoints,
        gradient,
        zoom=5,
        radius=21,
        blur=5).add_to(m)

m.save('StaticMap.html')




