import pymongo


client = pymongo.MongoClient("mongodb+srv://abepro:abepro@cluster0.0qzk3.mongodb.net/work?retryWrites=true&w=majority")
db = client.test