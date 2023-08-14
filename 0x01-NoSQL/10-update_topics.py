#!/usr/bin/env python3
"""Python function that changes all topics of a school document"""

def update_topics(mongo_collection, name, topics):
    """update many"""
    docs_to_find = {"name": name}
    updated_doc = {"topics": topics}
    mongo_collection.update_many(docs_to_find, {"$set": updated_doc})
