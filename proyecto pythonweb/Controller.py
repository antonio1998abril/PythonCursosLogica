import web
from Models import RegisterModel,LoginModel,Posts,UpdateModel
web.config.debug =False
urls= (
    '/','home',
    '/profile','Profile',
    '/update-settings','UpdateSettings',
    '/register','register',
    '/postregistro','PostRegistro',
    '/login','Login',
    '/check-login','CheckLogin',
    '/logout','Logout',
    '/post-activity','PostActivity',
    '/settings','Settings'

)
render = web.template.render("Views/Templates", base="Mainlayout")
app = web.application(urls,globals())
session= web.session.Session(app,web.session.DiskStore("session"), initializer={'user':None})
session_data = session._initializer

render = web.template.render("Views/Templates",base="Mainlayout", globals={'session': session_data,'current_user':session_data["user"]})
#class/routes
class home:
    def GET(self):
       # data= type('obj',(object,),{"username": "a","password":"a"})

        #login =LoginModel.LoginModel()
        #isCorrect= login.check_user(data)

        #if isCorrect:
            #session_data["user"]= isCorrect

        post_model =Posts.Posts()
        posts=post_model.get_all_post()

        return render.home(posts)

class register:
    def GET(self):
        return render.Register()
class PostRegistro:
    def POST(self):
        data=web.input()

        reg_model= RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username
class CheckLogin:
    def POST(self):
        data=web.input()

        login =LoginModel.LoginModel()
        iscorrect=login.check_user(data)

        if iscorrect:
            session_data["user"]=iscorrect
            return iscorrect

        return "error"

class Login:
    def GET(self):
        return render.Login()
    
class Logout:
    def GET(self):
        session ['user']=None
        session_data['user']=None
        session.kill()
        return 'success'

class PostActivity:
    def POST(self):
        data=web.input()
        data.username= session_data['user']['username']
        post_model=Posts.Posts()
        post_model.insert_post(data)
        return "success"
class UpdateSettings:
    def POST(self):
        data=web.input()
        data.username= session_data['user']['username']

        settings_model = UpdateModel.UpdateModel()
        if settings_model.update_info(data):
            return "success"
        else:
            return"ocurrio un error"    

class Settings:
    def GET(self):
        return render.Settings()
class Profile:
    def GET(self):
        return render.Profile()

class UserProfile:
    def GET (self,user):
        data =type('obj',(object,), {"username":"a","password":"a"})
        login =LoginModel.LoginModel()
        isCorrect= login.check_user(data)
        if isCorrect:
            session_data["user"]=isCorrect

        post_model=Posts.Posts()
        posts =post_model.get_user_posts(user)
        return render.Profile(posts)


       

if __name__ == "__main__":
    app.run()