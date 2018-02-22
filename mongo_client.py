#!coding=utf-8
from pymongo import MongoClient


class MyMongoClient():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.pymongo = MongoClient(host=self.ip, port=self.port)

    def get_document(self, db_name, collection_name, _id=None, condition=None):

        collection = self.pymongo.get_database(db_name).get_collection(collection_name)
        if _id is None and condition is None:
            return collection.find()
        if _id is not None:
            return collection.find_one(_id)
