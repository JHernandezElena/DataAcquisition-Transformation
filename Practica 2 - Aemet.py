api_key = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqdWxpbGlfOTdAaG90bWFpbC5jb20iLCJqdGkiOiJiNTE2ZTRlMy03ODQ5LTRhZWYtOTMwNC0zYTVkNjZhMzM4N2UiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTU3MTc2MDAxOCwidXNlcklkIjoiYjUxNmU0ZTMtNzg0OS00YWVmLTkzMDQtM2E1ZDY2YTMzODdlIiwicm9sZSI6IiJ9.hdl-fh0dVigVaF6WhKyca-6UmV11Dk7YgPoNtvVccZI"

import time
import requests

# Initialize variables.
BASE_URL = "https://opendata.aemet.es/opendata/api/valores/climatologicos/"
PAYLOAD = {"api_key": api_key}

##########################################
#         GET STATIONS INVENTORY         #
##########################################

# GET intermediate URL.
stations_url = BASE_URL + "inventarioestaciones/todasestaciones/"
intermediate_response = requests.get(stations_url, params = PAYLOAD)
time.sleep(2)

# GET stations inventory data.
data_url = intermediate_response.json()["datos"] #datos es la url que querias (para ver esto haz borramos
    #lo demas y lo de [datos] y hacemos print(data_url)
response = requests.get(data_url)
time.sleep(2)

# Parse stations inventory response.
target_station = "MADRID, CIUDAD UNIVERSITARIA"
#station_id = [item["indicativo"] for item in response.json() if item["nombre"] == target_station][0] es lo mismo que lo de abajo
for item in response.json():
    if item["nombre"] == target_station:
        targetid = item["indicativo"]
        break


##########################################
#         GET DAILY WEATHER DATA         #
##########################################

# Build URL.

initial_date = "2019-10-01T00:00:00UTC"
final_date = "2019-10-30T23:59:59UTC"
partial_url = "diarios/datos/fechaini/{0}/fechafin/{1}/estacion/{2}/"
weather_url = BASE_URL + partial_url.format(initial_date, final_date, station_id)

# GET intermediate URL.
intermediate_response = requests.get(weather_url, params = PAYLOAD)
time.sleep(2)

# GET station's weather data.
data_url = intermediate_response.json()["datos"]
response = requests.get(data_url)
print(response.text)
