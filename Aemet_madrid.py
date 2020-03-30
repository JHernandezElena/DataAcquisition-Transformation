import requests
url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/2019-10-01T00:00:00UTC/fechafin/2019-10-30T23:59:59UTC/estacion/3194U"

payload = {
 "api_key" : "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqdWxpbGlfOTdAaG90bWFpbC5jb20iLCJqdGkiOiJiNTE2ZTRlMy03ODQ5LTRhZWYtOTMwNC0zYTVkNjZhMzM4N2UiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTU3MTc2MDAxOCwidXNlcklkIjoiYjUxNmU0ZTMtNzg0OS00YWVmLTkzMDQtM2E1ZDY2YTMzODdlIiwicm9sZSI6IiJ9.hdl-fh0dVigVaF6WhKyca-6UmV11Dk7YgPoNtvVccZI"
}
response = requests.get(url, params=payload)

print(response.text)
print(response.status_code)