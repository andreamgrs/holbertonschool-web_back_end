#!/usr/bin/env python3
"""
"11-schools_by_topic.py" module
"""


def schools_by_topic(mongo_collection, topic):
    """
    function that returns the list of school having a specific topic:
    """
    if mongo_collection is None or not isinstance(topic, str):
        return []
    return list(mongo_collection.find({"topics": topic}))
