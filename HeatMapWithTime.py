# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 11:56:24 2022

@author: User
"""
import pandas as pd
data = pd.read_excel('data.xlsx') #, converters={'Index':int, 'TimeIndex':int,'Date':str,'Hour':int, 'CashPresentPercent': float, 'ATM_ID':str, 'Lattitude': float, 'Longitude': float  })
data['CashPresentPercent'] = 1 - data['CashPresentPercent'] / 100
print(data)


import folium
import folium.plugins as plugins
import matplotlib.pyplot as plt
from folium.plugins import HeatMap
from folium.plugins import HeatMapWithTime
import numpy as np
from datetime import datetime, timedelta


points = [data['Lattitude'], data['Longitude'], data['CashPresentPercent']]
points = np.array(points).T.tolist()

atm_0033 = points[2*60:3*60];
time_index=data['TimeIndex'].tolist()
time_index_033=time_index[2*60:3*60]
#time_index_033
len(time_index_033)
for index, value in enumerate(time_index):
    time_index[index] = int(value)


m=folium.Map([24,90])
HeatMap(atm_0033).add_to(m)

m.save('a.html')

# gradient1={ 0.0:'blue',
#             0.6: 'cyan',
#             0.7: 'lime',
#             0.8: 'yellow',
#             1.0: 'red'}

time_index=data['TimeIndex'].tolist()
time_index_033=time_index[2*60:3*60]
m2=folium.Map([24,90])
data_atm0033=[atm_0033] #[[[23.7335591, 90.3984233, 1.0], [23.7335591, 90.3984233, 0.82],[23.7335591, 90.3984233, 0.765]]]
hm=plugins.HeatMapWithTime(
   #data_atm0033,
    atm_0033,
    index=time_index_033,
    auto_play=False,
    max_opacity=1,
    gradient = {0.0:'red',
                0.6: 'yellow',
                0.7: 'lime',
                0.8: 'cyan',
                1.0: 'blue'},
    radius=21
    
)
hm.add_to(m2)
m2.save('b.html')

time_index=data['TimeIndex'].tolist()
time_index_033=time_index[2*60:3*60]
m2=folium.Map([24,90])
data_atm0033=[] # atm_0033 #[[[23.7335591, 90.3984233, 1.0], [23.7335591, 90.3984233, 0.82],[23.7335591, 90.3984233, 0.765]]]
for index, value in enumerate(atm_0033):
    data_atm0033.append([value])
hm=plugins.HeatMapWithTime(
   data_atm0033,
    #atm_0033,
    index=time_index_033,
    auto_play=False,
    max_opacity=1,
    gradient = {0.0:'red',
                0.6: 'yellow',
                0.7: 'lime',
                0.8: 'cyan',
                1.0: 'blue'},
    radius=21
    
)
hm.add_to(m2)
m2.save('c.html')

# import folium
# import folium.plugins as plugins
# import numpy as np
from datetime import datetime, timedelta

np.random.seed(3141592)
initial_data = (
    np.random.normal(size=(100, 2)) * np.array([[1, 1]]) +
    np.array([[48, 5]])
)

move_data = np.random.normal(size=(100, 2)) * 0.01

data = [(initial_data + move_data * i).tolist() for i in range(100)]

points_with_cash=[
        [90.4089993,24.2235923,77],         [90.3126342,24.0109028,50],         [90.3189091,23.9860764,98],
       
        ]
points=[
        [23.7938619,90.4043172, 0.0],         [23.7938619,90.4043172, 0.7],         [23.7938619,90.4043172, 1], 
        ]
data2 =  [    
    

		[    
				[46,5], [47,5]  , [47.5,5]  
		],
		[    
				[48,5], [49,5]    , [49.5, 5]
		],
    	[    
				[50,5], [51,5]    , [51.5, 5]
		],

]
data2=[]
data2 =  [    
       points, #[[23.7938619,90.4043172, 0.0],[23.7938619,90.4043172, 0.7],[23.7938619,90.4043172, 1]]
       points,
    points,
    points,
    points,
    points,
    points,
    
]


#m = folium.Map([48., 5.], tiles='stamentoner', zoom_start=6)
#hm = plugins.HeatMapWithTime(data2)
#hm.add_to(m)
"""
time_index = [
    (datetime.now() + k * timedelta(1)).strftime('%Y-%m-%d') for
    k in range(len(data2))
]
time_index = list(range(len(data2)))
"""
time_index = [0,1,2,3,4,5,6]


m3 = folium.Map([48., 5.], zoom_start=6)

hm = plugins.HeatMapWithTime(
    data2, #[[[1,2],[3,4]]]
    index=time_index,
    auto_play=True,
    max_opacity=0.6,
    radius=21,
    gradient = {0.0:'blue',
                0.6: 'cyan',
                0.7: 'lime',
                0.8: 'yellow',
                1.0: 'red'}
    
)

hm.add_to(m3)
m3.save('d.html')







