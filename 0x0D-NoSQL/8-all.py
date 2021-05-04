#!/usr/bin/env python3
"""[lists all documents in a collection]
"""
import pymongo


def list_all(mongo_collection):
    """[list_all]

    Args:
        mongo_collection ([pymongo collection object]): [collection of docs]

    Returns:
        [list]: [empty list if no document in the collection or list of docs]
    """
    docs = mongo_collection.find()
    return [doc for doc in docs]
