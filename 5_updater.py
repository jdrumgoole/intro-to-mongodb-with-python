import pprint

import pymongo
from mimesis import Person


# Connection object
c = pymongo.MongoClient(
    host="mongodb+srv://livedemo:livedemo@livedemo.atyas.mongodb.net/test_db?retryWrites=true&w=majority")

# database object
database = c["test_db"]

# collection/table object
collection = database["users"]

p = Person("en", seed=0xBEEF)
person = {"name": p.first_name(),
          "surname": p.surname(),
          "email": p.email(),
          "password": p.password()}

collection.insert_one(person)
print("Inserted:")
pprint.pprint(person)

collection.update_one({"_id": person["_id"]}, {"$set": {"session_id": 20}})
collection.update_one({"_id": person["_id"]}, {"$push": {"assets": {"laptop": "MacPro"}}})
doc = collection.find_one({"_id": person["_id"]})
print("Updated:")
pprint.pprint(doc)
