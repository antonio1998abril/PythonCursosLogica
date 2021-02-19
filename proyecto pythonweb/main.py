import web

urls = (
    "/(.*)","index"
)
render = web.template.render("src/")
app =web.application(urls, globals())
class index:
    def GET(self,name):
        return 'hola'

if __name__ == "__main__":
    app.run()


