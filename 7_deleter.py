import pprint

import pymongo

# Connection object
c = pymongo.MongoClient(
    host="mongodb+srv://livedemo:livedemo@livedemo.atyas.mongodb.net/test_db?retryWrites=true&w=majority")

# database object
database = c["test_db"]

# collection/table object
collection = database["users"]

count = collection.count_documents({"surname": "Glover"})
print(f"There are {count} 'Glovers'")
deleted_results = collection.delete_many({"surname": "Glover"})
print(f"We deleted all ({deleted_results.deleted_count}) the 'Glovers'")
count = collection.count_documents({"surname": "Glover"})
print(f"{count} 'Glover's left")
