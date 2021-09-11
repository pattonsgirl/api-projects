import csv
import time
import requests
import numpy as np

# putting the usernames and ips into a list so I can use them later
with open("data/auth.logs.csv", 'r') as f:
    reader = csv.reader(f)
    usernames, ips = [], []

    for row in reader:
        usernames.append(row[0].strip())
        ips.append(row[1].strip())

# print first 10 as proof
print(ips[:10])
print(len(ips))

# remove duplicate ips
nd_ips = []
for ip in ips:
    if ip not in nd_ips:
        nd_ips.append(ip)

lats, lons = [],[]

for ip in nd_ips:
    # need to slow down API requests
    time.sleep(0.2)

    response = requests.get("https://ipinfo.io/"+ip)

    loc = response.json()['loc']
    print(loc)
    lats.append(float(loc.split(",")[0]))
    lons.append(float(loc.split(",")[1]))

#print(lats[:10])
#print(lons[:10])

#for num in lats:

lat_lons = []

for num in np.arange(len(lats)):
    # TODO: append ip as well?  Pandas prep?
    lat_lons.append([nd_ips[num], lats[num], lons[num]])

#print(lat_lons)
with open("data/ip-latlons.csv", 'w', newline='') as f:
    write = csv.writer(f)
    for num in np.arange(len(lat_lons)):
        write.writerow(lat_lons[num])
