#!/usr/bin/env python3
"""Module to get all documents"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Lists all documents in a collection

    :param mongo_collection: collection object
    :return: List of all documents or empty list if none
    """
    documents = list(mongo_collection.find())
    return documents
