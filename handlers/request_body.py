import json

import tornado.web
from sqlalchemy.orm import sessionmaker

from db import engine
from models import Request, check_for_request_duplicates
import base64

Session = sessionmaker(bind=engine)


def get_key(body):
    str_to_encode = ''
    for key, value in body.items():
        str_to_encode += key + value
    encoded_key = str(
        base64.b64encode(
            bytes(
                str_to_encode.encode('utf8')
            )
        )
    ).lstrip("b'").rstrip("'")
    return encoded_key


class GetRequestBodyHandler(tornado.web.RequestHandler):
    async def get(self):
        session = Session()
        old_key = self.get_query_argument('key')
        request_object = session.query(Request).get(
            {'key': old_key}
        )
        if request_object is None:
            self.set_status(404)
            return self.write(json.dumps({"Error": "not found"}))
        return self.write(json.dumps(request_object.serialize))


class PostRequestBodyHandler(tornado.web.RequestHandler):
    async def post(self):
        session = Session()
        body = tornado.escape.json_decode(self.request.body)
        key = get_key(body)
        request_object = Request(
            key=get_key(body),
            data=json.dumps(body)
        )
        duplicates_count = check_for_request_duplicates(key)
        if duplicates_count > 0:
            request_object = session.query(Request).get(
                {'key': key}
            )
            request_object.update_duplicates()
        session.add(request_object)
        session.commit()
        return self.write(json.dumps(request_object.serialize))


class PutRequestBodyHandler(tornado.web.RequestHandler):
    async def put(self):
        session = Session()
        old_key = self.get_query_argument('key')
        body = tornado.escape.json_decode(self.request.body)
        request_object = session.query(Request).get(
            {'key': old_key}
        )
        if request_object is None:
            self.set_status(404)
            return self.write(json.dumps({"Error": "not found"}))
        request_object.update(
            key=get_key(body),
            data=json.dumps(body)
        )
        session.add(request_object)
        session.commit()
        return self.write(json.dumps(request_object.serialize))


class DeleteRequestBodyHandler(tornado.web.RequestHandler):
    async def delete(self):
        session = Session()
        old_key = self.get_query_argument('key')
        request_object = session.query(Request).get(
            {'key': old_key}
        )
        if request_object is None:
            self.set_status(404)
            return self.write(json.dumps({"Error": "not found"}))
        session.delete(request_object)
        session.commit()
        return self.write(json.dumps(request_object.serialize))