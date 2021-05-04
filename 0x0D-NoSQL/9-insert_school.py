#!/usr/bin/env python3
"""[inserts a new document in a collection based on kwargs]
"""


def insert_school(mongo_collection, **kwargs):
    """[insert_school]

    Args:
        mongo_collection ([pymongo collection object]): [collection of docs]

    Returns:
        [int]: [new _id]
    """
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
