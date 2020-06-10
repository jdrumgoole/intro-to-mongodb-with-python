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
distinct_first_names = collection.distinct("name")
for name in distinct_first_names:
    print(name)
print(f'{len(distinct_first_names)} first names')
