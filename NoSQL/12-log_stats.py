#!/usr/bin/env python3
"""
"12-log_stats.py" module
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    """
    provides stats about Nginx logs stored in MongoDB
    """

    total = collection.count_documents({})
    print(f"{total} logs")

    # methods count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # status check
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")
