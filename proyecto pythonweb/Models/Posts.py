from pymongo import MongoClient

class Posts:
    def __init__ (self):
        self.client=MongoClient()
        #conexion a la base de datos
        self.db=self.client.codewizard
        self.Users=self.db.users
        self.Posts= self.db.posts

    def insert_post(self,data):
        inserted=self.Posts.insert({"username":data.username, "content":data.content})
        return True

    def get_all_post(self):
        all_post =self.Posts.find()
        new_posts=[]

        for post in  all_post:
            post["user"]= self.Users.find_one({"username":post["username"]})
            new_posts.append(post)
        return new_posts

    def get_user_posts(self,user):
        all_posts = self.Posts.find({"username":user}).sort("date_added",-1)
        new_posts=[]

        for post in all_posts:
            print(post)
            post["user"]=self.Users.fin_one({"username":post["username"]})
            new_posts.append(post)
        return new_posts