#!/usr/bin/env python3
"""Python function that returns the list of school"""

def schools_by_topic(mongo_collection, topic):
    """get schools by topic"""
    return mongo_collection.find({"topics":  {"$in": [topic]}})

