from pymongo import MongoClient

conn = MongoClient("mongodb+srv://admin:iW70CzDypD5z8Kr5@api.uq5l2w9.mongodb.net/Covid_Data?retryWrites=true&w=majority")
db = conn.get_database('Covid_Data')
collection_name = db["Cases"]
