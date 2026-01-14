#!/usr/bin/env python3
"""
"10-update_topics.py" module
"""


def update_topics(mongo_collection, name, topics):
    """
    function that changes all topics of a school document based on the name
    """
    if mongo_collection is None or not name or not isinstance(topics, list):
        return
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
