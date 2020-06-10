import pymongoshell
c = pymongoshell.MongoClient(
    host="mongodb+srv://livedemo:livedemo@livedemo.atyas.mongodb.net/test_db?retryWrites=true&w=majority")
c.collection = "test_db.users"
c.distinct("surname")
c.find()
c.find(filter={}, projection={"_id": 0, "password": 0})
c.find_one({"surname": "Taylor"})
c.aggregate([{"$match": {"surname": "Taylor"}}, {"$count": "Taylor_as_a_surname"}])
