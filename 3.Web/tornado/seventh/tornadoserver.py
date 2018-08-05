from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options, define, parse_config_file
from seventh.app.myapp import MyApplication, IndexHandler, LoginHandler, BlogHandler, RegistHandler, LoginModule, \
    BlogModule, RegistModule

define('duankou',type=int,default=8888)
parse_config_file('../config/config')
app = MyApplication(hs=[('/',IndexHandler),
                            ('/login',LoginHandler),
                            ('/blog',BlogHandler),
                            ('/regist',RegistHandler)],
                  tp='mytemplate',
                  sp='mystatics',
                  um={'loginmodule':LoginModule,
                              'blogmodule':BlogModule,
                              'registmodule':RegistModule})
server = HTTPServer(app)
server.listen(options.duankou)
IOLoop.current().start()