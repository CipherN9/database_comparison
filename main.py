from pymongo import MongoClient
from pprint import pprint
from bson import SON

db = MongoClient().aggregation_example
# result = db.things.insert_many(
#     [
#         {"x": 1, "tags": ["dog", "cat"]},
#         {"x": 2, "tags": ["cat"]},
#         {"x": 2, "tags": ["mouse", "cat", "dog"]},
#         {"x": 3, "tags": []},
#     ]
# )
# result.inserted_ids
# for thing in db.things.find():
#     pprint(thing)

pipeline = [{"$unwind": "$tags"}]
pprint(list(db.things.aggregate(pipeline)))
print("\n")
pipeline = [{"$unwind": "$tags"},
            {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
            {"$sort": SON([("count", 1)])}
            ]
pprint(list(db.things.aggregate(pipeline)))