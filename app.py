from http.client import HTTPResponse
import json
from typing import Collection
import requests 
from flask import Flask
import pymongo

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def home_page_route():
    home_page_welcome = "ブロードキャスト サーバーへようこそ。クエリがある場合は、指定されたパスに移動してください。ブロードキャストをご利用いただきありがとうございます。サイン放送を続けて、私たちをサポートし続けてください。ありがとうございました"
    json_dumps = json.dumps(home_page_welcome)
    return json_dumps 


@app.route('/update news/', methods = ['GET'])
def update_news():
    news_api_org_news_link = "https://newsapi.org/v2/everything?q=business&from=2022-09-26&sortBy=popularity&apiKey=da8a1fc3db81419fb110802cb65f7da0"
    news_api_org_news_link_entertainment = "https://newsapi.org/v2/everything?q=entertainment&from=2022-09-26&sortBy=popularity&apiKey=da8a1fc3db81419fb110802cb65f7da0"
    news_api_org_news_link_general = "https://newsapi.org/v2/everything?q=general&from=2022-09-26&sortBy=popularity&apiKey=da8a1fc3db81419fb110802cb65f7da0"
    news_api_org_news_link_health = "https://newsapi.org/v2/everything?q=health&from=2022-09-26&sortBy=popularity&apiKey=da8a1fc3db81419fb110802cb65f7da0"
    news_api_org_news_link_science = "https://newsapi.org/v2/everything?q=science&from=2022-09-26&sortBy=popularity&apiKey=da8a1fc3db81419fb110802cb65f7da0"
    news_api_org_news_link_sports = "https://newsapi.org/v2/everything?q=sports&from=2022-09-26&sortBy=popularity&apiKey=da8a1fc3db81419fb110802cb65f7da0"
    news_api_org_news_link_technology = "https://newsapi.org/v2/everything?q=technology&from=2022-09-26&sortBy=popularity&apiKey=da8a1fc3db81419fb110802cb65f7da0"
    news_york_times_news_link = "https://api.nytimes.com/svc/topstories/v2/world.json?api-key=3JDgavYvlfGwaSiOnAOo1sHFIwa0e0ty"
    req = requests.get(news_api_org_news_link)
    req3 = requests.get(news_api_org_news_link_entertainment)
    req4 = requests.get(news_api_org_news_link_general)
    req5 = requests.get(news_api_org_news_link_health)
    req6 = requests.get(news_api_org_news_link_science)
    req7 = requests.get(news_api_org_news_link_sports)
    req8 = requests.get(news_api_org_news_link_technology)
    
    req2 = requests.get(news_york_times_news_link)
    
    new_api_org_data = req.json()
    new_api_org_data1 = req3.json()
    new_api_org_data2 = req4.json()
    new_api_org_data3 = req5.json()
    new_api_org_data4 = req6.json()
    new_api_org_data5 = req7.json()
    new_api_org_data6 = req8.json()
    
    new_york_news = req2.json()

    client = pymongo.MongoClient("mongodb+srv://broadcast_server_access:123qpa456lzm@broadcast.eevngdm.mongodb.net/test")
    print(client)
    db = client["broadcast_api"]
    collection = db["news_feed"]
    x = collection.delete_many({})
    for i in range(len(new_api_org_data["articles"])):
        dict = {
            "title" : new_api_org_data["articles"][i]["title"] , 
            "author" : new_api_org_data["articles"][i]["author"],
            "description" : new_api_org_data["articles"][i]["description"],
            "image url" : new_api_org_data["articles"][i]["urlToImage"],
            "url" : new_api_org_data["articles"][i]["url"],
            "likes" : "",
            "comment" : ""
        }
        collection.insert_one(dict)
    for i in range(len(new_api_org_data1["articles"])):
        dict = {
            "title" : new_api_org_data["articles"][i]["title"] , 
            "author" : new_api_org_data["articles"][i]["author"],
            "description" : new_api_org_data["articles"][i]["description"],
            "image url" : new_api_org_data["articles"][i]["urlToImage"],
            "url" : new_api_org_data["articles"][i]["url"],
            "likes" : "",
            "comment" : ""
        }
        collection.insert_one(dict)
    for i in range(len(new_api_org_data2["articles"])):
        dict = {
            "title" : new_api_org_data["articles"][i]["title"] , 
            "author" : new_api_org_data["articles"][i]["author"],
            "description" : new_api_org_data["articles"][i]["description"],
            "image url" : new_api_org_data["articles"][i]["urlToImage"],
            "url" : new_api_org_data["articles"][i]["url"],
            "likes" : "",
            "comment" : ""
        }
        collection.insert_one(dict)
    for i in range(len(new_api_org_data3["articles"])):
        dict = {
            "title" : new_api_org_data["articles"][i]["title"] , 
            "author" : new_api_org_data["articles"][i]["author"],
            "description" : new_api_org_data["articles"][i]["description"],
            "image url" : new_api_org_data["articles"][i]["urlToImage"],
            "url" : new_api_org_data["articles"][i]["url"],
            "likes" : "",
            "comment" : ""
        }
        collection.insert_one(dict)
    for i in range(len(new_api_org_data4["articles"])):
        dict = {
            "title" : new_api_org_data["articles"][i]["title"] , 
            "author" : new_api_org_data["articles"][i]["author"],
            "description" : new_api_org_data["articles"][i]["description"],
            "image url" : new_api_org_data["articles"][i]["urlToImage"],
            "url" : new_api_org_data["articles"][i]["url"],
            "likes" : "",
            "comment" : ""
        }
        collection.insert_one(dict)
    for i in range(len(new_api_org_data5["articles"])):
        dict = {
            "title" : new_api_org_data["articles"][i]["title"] , 
            "author" : new_api_org_data["articles"][i]["author"],
            "description" : new_api_org_data["articles"][i]["description"],
            "image url" : new_api_org_data["articles"][i]["urlToImage"],
            "url" : new_api_org_data["articles"][i]["url"],
            "likes" : "",
            "comment" : ""
        }
        collection.insert_one(dict)
    for i in range(len(new_api_org_data6["articles"])):
        dict = {
            "title" : new_api_org_data["articles"][i]["title"] , 
            "author" : new_api_org_data["articles"][i]["author"],
            "description" : new_api_org_data["articles"][i]["description"],
            "image url" : new_api_org_data["articles"][i]["urlToImage"],
            "url" : new_api_org_data["articles"][i]["url"],
            "likes" : "",
            "comment" : ""
        }
        collection.insert_one(dict)
    
    json_data_1 = json.dumps("Updated Sucessfully")
    
    return json_data_1
    


if __name__ == "__main__":
    app.run(debug=True)