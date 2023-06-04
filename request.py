import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'sepal length (cm)':5.1, 'sepal width (cm)':3.5, 'petal length (cm)':1.4, 'petal width (cm)':0.2})

print(r.json())