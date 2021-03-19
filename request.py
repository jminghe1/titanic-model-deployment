import requests
import json

url ='http://127.0.0.1:5000/predict'
dictionary = {'Age':50, 'SipSp':1, 'Parch':1,'Fare':150,'Sex_male':1,'Cabin_Rare':0,'Embarked_S':1}

r = requests.post(url, json=dictionary)
print(r.json())