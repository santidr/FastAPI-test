from pymongo import MongoClient

mongoURI = 'mongodb://localhost:27017'
client = MongoClient(mongoURI)

db = client['fastdb_test']