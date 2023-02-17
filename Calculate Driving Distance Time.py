import requests
import json
import datetime

def Calculate_Driving_Distance_Time(lat,lon , lat2,lon2):
    r = requests.get(f"http://router.project-osrm.org/route/v1/car/{lon_1},{lat};{lon_2},{lat_2}?overview=false""")# then you load the response using the json libray

    print(f"http://router.project-osrm.org/route/v1/car/{lon},{lat};{lon2},{lat2}?overview=false""")

    routes = json.loads(r.content)
    route_1 = routes.get("routes")[0]

    time = str(datetime.timedelta(seconds=route_1["duration"]))
    Distance = route_1["distance"]

    #Converte Disance to km
    Distance = float(Distance / 1000)
    print(Distance , "km")
    print(time , "DD:MM:SS")



lon_1 = 35.014987
lat = 32.787691

lon_2 = 35.014987
lat_2= 32.779052

Calculate_Driving_Distance_Time(lat , lon_1 , lat_2 , lon_2)