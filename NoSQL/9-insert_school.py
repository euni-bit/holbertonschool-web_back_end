#!/usr/bin/env python3
""" function that inserts a new document in a collection"""


def insert_school(mongo_collection: object, **kwargs):
    """function that inserts a new document in a collection"""
    data = mongo_collection.insert_one({**kwargs})
    return data.inserted_id