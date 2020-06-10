import pprint
import argparse

import pymongo

# Connection object
c = pymongo.MongoClient(
    host="mongodb+srv://livedemo:livedemo@livedemo.atyas.mongodb.net/test_db?retryWrites=true&w=majority")

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
    print("Delete index on field 'surname'")
    collection.drop_index("surname_1")

doc = collection.find({"surname": "Atkinson"}).explain()
pprint.pprint(doc)
