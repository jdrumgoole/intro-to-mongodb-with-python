import pprint
import argparse

import pymongo

# Connection object
c = pymongo.MongoClient(
    host="http://localhost:27017")

# database object
database = c["test_db"]

# collection/table object
collection = database["users"]

parser = argparse.ArgumentParser()
parser.add_argument("--createindex", default=False, action="store_true")
parser.add_argument("--deleteindex", default=False, action="store_true")
args = parser.parse_args()

if args.createindex:
    print("create index on field 'surname'")
    collection.create_index("surname")

if args.deleteindex:
    if args.deleteindex in list(collection.list_indexes()):
        print("Delete index on field 'surname'")
        collection.drop_index("surname_1")

# An explain plan looks at a query's performance
doc = collection.find({"surname": "Atkinson"}).explain()
pprint.pprint(doc)
