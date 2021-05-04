#!/usr/bin/env python3
"""[changes all topics of a school document based on the name]
"""


def update_topics(mongo_collection, name, topics):
    """[update_topics]

    Args:
        mongo_collection ([pymongo collection object]): [collection of docs]
        name ([str]): [school name to update]
        topics ([list]): [topics approached in the school]
    """
    query = {"name": name}
    values = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, values)
