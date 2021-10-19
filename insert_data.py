import json
from pymongo import MongoClient

client =  MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
db = client['Greendeck_db']
collection = db['data']

with open('Greendeck.json') as f:
    file_data = json.load(f)
    
res=collection.insert_many(file_data)

data = db.data.find() 
animals = [{"name": animal["name"], "type": animal["regular_price_value"]} for animal in data]
print(animals,data)
client.close()
