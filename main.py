import tornado.ioloop
import tornado.web
from db import engine
from sqlalchemy.orm import sessionmaker

from handlers import request_body, statistic
Session = sessionmaker(bind=engine)

def make_app():
    return tornado.web.Application([
        (r"/api/add", request_body.PostRequestBodyHandler),
        (r"/api/get", request_body.GetRequestBodyHandler),
        (r"/api/put", request_body.PutRequestBodyHandler),
        (r"/api/delete", request_body.DeleteRequestBodyHandler),
        (r"/api/statistic", statistic.GetStatisticHandler),
    ],
    debug=True)


def main():
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()