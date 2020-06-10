from datetime import datetime
import argparse

import pymongo
from mimesis import Person
import gc


def insert_one_at_a_time(col, total):
    start_time = datetime.utcnow()
    p = Person("en", seed=0xBEE)
    for i in range(total):
        proxy_person = {"name": p.first_name(),
                        "surname": p.surname(),
                        "email": p.email(),
                        "password": p.password()}
        col.insert_one(proxy_person)
        if ((i+1) % 10) == 0:
            print(f"Inserted {i+1} docs")
    end_time = datetime.utcnow()
    duration = end_time - start_time
    print(f"Inserting {i + 1} records took {duration}")


def insert_in_batches(col, total, batch_size):
    many_people = []
    inserted_count = 0
    start_time = datetime.utcnow()
    previous_time = start_time
    p = Person("en", seed=0xBEE)
    for i in range(total):
        proxy_person = {"name": p.first_name(),
                        "surname": p.surname(),
                        "email": p.email(),
                        "password": p.password()}
        many_people.append(proxy_person)
        if (len(many_people) % batch_size) == 0:
            col.insert_many(many_people)
            inserted_count = inserted_count + len(many_people)
            time_now = datetime.utcnow()
            elapsed_time = time_now - previous_time
            previous_time = time_now
            print(f"Inserted {len(many_people)} people in {elapsed_time}")
            many_people.clear()
            gc.collect()
    if len(many_people) > 0:
        col.insert_many(many_people)
        inserted_count = inserted_count + len(many_people)
    end_time = datetime.utcnow()
    duration = end_time - start_time
    print(f"Inserting {inserted_count} records took {duration}")


parser = argparse.ArgumentParser()
parser.add_argument("--insertmany", default=False, action="store_true")
parser.add_argument("--insertone", default=False, action="store_true")
parser.add_argument("--both", default=False, action="store_true")
parser.add_argument("--collection", default="devnull")
parser.add_argument("--total", type=int, default=100)
parser.add_argument("--batch", type=int, default=500)
parser.add_argument("--drop", default=False, action="store_true")

args = parser.parse_args()

c = pymongo.MongoClient(
    host="mongodb+srv://livedemo:livedemo@livedemo.atyas.mongodb.net/test_db?retryWrites=true&w=majority")

database = c["test_db"]
collection = database[args.collection]

if args.drop:
    collection.drop()

if args.both:
    print("(both) insert_one")
    insert_one_at_a_time(collection, args.total)
    print("(both) insert_many")
    insert_in_batches(collection, args.total, args.batch)

if args.insertone:
    print("insert_one")
    insert_one_at_a_time(collection, args.total)

if args.insertmany:
    print("insert_many")
    insert_in_batches(collection, args.total, args.batch)
