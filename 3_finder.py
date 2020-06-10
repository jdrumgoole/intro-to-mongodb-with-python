import pymongo
c = pymongo.MongoClient(
    host="mongodb+srv://livedemo:livedemo@livedemo.atyas.mongodb.net/test_db?retryWrites=true&w=majority")
db = c["test_db"]
collection=db["users"]
collection.find_one()
collection.find()

import pymongoshell
c = pymongoshell.MongoClient(
    host="mongodb+srv://livedemo:livedemo@livedemo.atyas.mongodb.net/test_db?retryWrites=true&w=majority")
c.collection = "test_db.users"
c.find()
c.find(filter={}, projection={"_id": 0, "password": 0})
c.find(filter={}, projection={"_id": 0, "email": 1})
c.find_one({"surname": "Taylor"})
c.aggregate([{"$match": {"surname": "Taylor"}}, {"$count": "Taylor_as_a_surname"}])
