import pymongo, bcrypt
from pymongo import MongoClient

class UpdateModel:
    def __init__ (self):
        self.client=MongoClient()
        self.db=self.client.codewizard
        self.Users=self.db.users

    def update_info(self,data):
            updated= self.Users.update_one({
            "username":data["username"]
        }, {"$set":data},upsert=False)
            return True