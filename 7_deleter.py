import pprint

import pymongo

# Connection object
c = pymongo.MongoClient(
    host="http://localhost:27017")

# database object
database = c["test_db"]

# collection/table object
collection = database["users"]

count = collection.count_documents({"surname": "Glover"})
print(f"There are {count} 'Glovers'")
delete_one_result = collection.delete_one({"surname": "Glover"})
count = collection.count_documents({"surname": "Glover"})
print(f"{count} 'Glover's left after delete_one")

deleted_results = collection.delete_many({"surname": "Glover"})
print(f"We deleted all ({deleted_results.deleted_count}) the 'Glovers'")
count = collection.count_documents({"surname": "Glover"})
print(f"{count} 'Glover's left")
