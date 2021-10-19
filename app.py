from flask import Flask, jsonify,render_template,request,redirect,url_for
import pymongo
from bson import ObjectId 
from pymongo import MongoClient

app = Flask(__name__)

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
    db = client["Greendeck_db"]
    db = db['data']
    return db


#Home page

@app.route('/')
def ping_server():
    db = get_db()
    data = db.find()
    return render_template('index.html',data=data)
 
 
#Adding a View    
@app.route("/add")    
def add(): 
    return render_template('add.html')  

#Adding a Data      
@app.route("/add", methods=['POST'])    
def action ():  
    db = get_db() 
    name=request.values.get("name")    
    brand_name=request.values.get("brand_name")    
    regular_price_value=request.values.get("regular_price_value")    
    offer_price_value=request.values.get("offer_price_value") 
    currency=request.values.get("currency")   
    classification_l1=request.values.get("classification_l1") 
    db.insert({ "name":name, "brand_name":brand_name, "regular_price_value":regular_price_value, "offer_price_value":offer_price_value,"currency":currency, "classification_l1":classification_l1})    
    return redirect("/")    


#Deleting a data   

@app.route("/remove")    
def remove ():    
    db = get_db() 
    key=request.values.get("_id")    
    db.remove({"_id":ObjectId(key)})    
    return redirect("/")  


#Updating a Data    

@app.route("/update")    
def update (): 
    db = get_db() 
    id=request.values.get("_id")    
    task=db.find({"_id":ObjectId(id)})    
    return render_template('update.html',task=task)        
  
  
#Updating a Data     

@app.route("/update_action", methods=['POST'])    
def action3 (): 
    db = get_db() 
    name=request.values.get("name")    
    brand_name=request.values.get("brand_name")    
    regular_price_value=request.values.get("regular_price_value")    
    offer_price_value=request.values.get("offer_price_value")   
    classification_l1=request.values.get("classification_l1") 
    id=request.values.get("_id")    
    db.update({"_id":ObjectId(id)}, {'$set':{ "name":name, "brand_name":brand_name, "regular_price_value":regular_price_value, "offer_price_value":offer_price_value,"classification_l1":classification_l1 }})    
    return redirect("/")   

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)

