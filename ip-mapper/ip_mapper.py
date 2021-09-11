from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import csv

with open("data/ip-latlons.csv", 'r') as f:
    reader = csv.reader(f)
    ips, lats, lons = [], [],[]

    for row in reader:
        ips.append(row[0])
        lats.append(float(row[1]))
        lons.append(float(row[2]))

# print first 10 as proof
#print(lats[:10])
#print(len(lats))

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': ips,
    'marker': {
        #'colorscale': 'Viridis',
        'reversescale': True,
        'color':'MediumPurple',
        'size': 15,
        'line':{
            'color':'Purple',
            'width': 2,
        }
    },
}]

figure_layout = Layout(title='IP Sources')

fig = {
    'data': data, 
    'layout': figure_layout
}

offline.plot(fig, filename='images/ip-sources.html')