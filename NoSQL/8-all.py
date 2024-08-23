#!/usr/bin/env python3
"""List all documents in a collection"""


def list_all(mongo_collection: object) -> list:
    """List all documents in a collection"""
    return mongo_collection.find({}) if mongo_collection.find({}) else []