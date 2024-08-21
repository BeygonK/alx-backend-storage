#!/usr/bin/env python3
"""Function to insert a new document"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a collection

    :param mongo_collection: collection object
    :param kwargs: represents document to be inserted
    :return: _id of newly inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
