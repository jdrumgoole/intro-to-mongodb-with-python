"""
Author : joe@joedrumgoole.com

MPing : Ping a MongoDB server with an is_master command.

"""

import pymongo
from pymongo.errors import ConnectionFailure, ConfigurationError
from datetime import datetime
import pprint
import sys

if __name__ == "__main__":

    arg = None
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = "mongodb+srv://livedemo:livedemo@livedemo.atyas.mongodb.net/?retryWrites=true&w=majority"
    try:
        client = pymongo.MongoClient(host=host)
        # The is_master command is cheap and does not require auth. admin
        # is always a db.
        doc = client.admin.command('hello')
        pprint.pprint(doc)

    except ConnectionFailure as e:
        print(f"Server '{host}' not available: {e}")
    except ConfigurationError as e:
        print(f"Server '{host}' not available: {e}")
