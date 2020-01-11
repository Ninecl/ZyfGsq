import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


class HomepageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('homepage.html')


class StoryHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('story.html')

class GalleryHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('gallery.html')


class gallery_1(tornado.web.RequestHandler):
    def get(self):
        self.render('gallery_1.html')


class gallery_2(tornado.web.RequestHandler):
    def get(self):
        self.render('gallery_2.html')


class gallery_5(tornado.web.RequestHandler):
    def get(self):
        self.render('gallery_5.html')


class gallery_7(tornado.web.RequestHandler):
    def get(self):
        self.render('gallery_7.html')


class gallery_9(tornado.web.RequestHandler):
    def get(self):
        self.render('gallery_9.html')


class SigninHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('signin.html')


class SayHandler(tornado.web.RequestHandler):
    def get(self):
        password = self.get_argument("password")
        if password == 'Lancelot7923':
            self.render("say.html")
        else:
            print("no")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', HomepageHandler),
            (r'/story', StoryHandler),
            (r'/gallery', GalleryHandler),
            (r'/gallery_1', gallery_1),
            (r'/gallery_2', gallery_2),
            (r'/gallery_5', gallery_5),
            (r'/gallery_7', gallery_7),
            (r'/gallery_9', gallery_9),
            (r'/signin', SigninHandler),
            (r'/say', SayHandler)
        ]
        settings = {
            'template_path': 'templates',
            'static_path': 'static'
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()    
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(80)
    tornado.ioloop.IOLoop.instance().start()

