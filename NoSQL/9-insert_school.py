#!/usr/bin/env python3
"""
"9-insert_school.py" module
"""


def insert_school(mongo_collection, **kwargs):
    """
     function that inserts a new document in a collection based on kwargs
    """
    if mongo_collection is None or not kwargs:
        return None
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
