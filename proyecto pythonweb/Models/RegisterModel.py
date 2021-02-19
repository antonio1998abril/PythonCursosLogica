from pymongo import MongoClient
import bcrypt
class RegisterModel:
    def __init__ (self):
        self.client=MongoClient()
        #conexion a la base de datos
        self.db=self.client.codewizard
        self.Users=self.db.users

    def insert_user(self,data):
        hashed=bcrypt.hashpw(data.password.encode(),bcrypt.gensalt())
        id=self.Users.insert({"username":data.username,"name": data.name,"password":hashed,"email":data.email,"hobbies":data.hobbies,"about":data.about})
        print("El id es",id)

        myuser=self.Users.find_one({"username":data.username})


        if bcrypt.checkpw("sssss".encode(),myuser["password"]):
            print("concuerda")