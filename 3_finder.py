import pymongo
c = pymongo.MongoClient(
    host="http://localhost:27017")
db = c["test_db"]
collection=db["users"]
collection.find_one()
collection.find()

