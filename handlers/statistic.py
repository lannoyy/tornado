import json

import tornado.web
from sqlalchemy.orm import sessionmaker

from db import engine
from models import Request
Session = sessionmaker(bind=engine)


class GetStatisticHandler(tornado.web.RequestHandler):
    async def get(self):
        session = Session()
        request_objects = session.query(Request).all()
        total_count = len(request_objects)
        total_duplicate = 0
        for request_object in request_objects:
            total_duplicate += request_object.duplicates
        total_count += total_duplicate
        try:
            duplicate_to_requests = int((total_duplicate/total_count) * 100)
        except ZeroDivisionError:
            duplicate_to_requests = "Total_duplicate_or_count = 0"
        output = {
            'total_count': total_count,
            'total_duplicate': total_duplicate,
            'duplicate_to_requests': duplicate_to_requests
        }
        return self.write(json.dumps(output))
