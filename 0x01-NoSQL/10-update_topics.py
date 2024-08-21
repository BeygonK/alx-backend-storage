#!/usr/bin/env python3
"""Function to change all topics of school"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Update topics of a school based on a name

    :param mongo_collection: collection object
    :param name: school name to update
    :param topics: topics to set
    :return: None
    """
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
    )
