import pprint

import pymongo
from mimesis import Person


# Connection object
c = pymongo.MongoClient(
    host="http://localhost:27017")

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
collection.update_one({"_id": person["_id"]}, {"$push": {"phone": {"cell": "+1 123456789"}}})
doc = collection.find_one({"_id": person["_id"]})
print("Updated:")
pprint.pprint(doc)

collection.update_many({"surname": "Taylor"}, {"$push": {"assets": {"laptop": "MacPro laptop"}}})
laptop_count = collection.count_documents({"surname": "Taylor", "assets.laptop": "MacPro laptop"})
print(f"We have allocated {laptop_count} laptops")

