import requests
url = "http://www.linkedin.com/in/juliahernandezelena/"

response = requests.get(url)
response.status_code

