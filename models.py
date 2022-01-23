from sqlalchemy import (
    Column, Integer, String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

from db import engine

Session = sessionmaker(bind=engine)

Base = declarative_base()


class Request(Base):
    __tablename__ = 'request'
    key = Column(
        String,
        nullable=False,
        primary_key=True
    )
    data = Column(
        String,
        nullable=False
    )
    duplicates = Column(
        Integer,
        nullable=True
    )

    def __init__(self, key: str, data: str):
        self.key = key
        self.data = data
        self.duplicates = 0

    def update(self, key: str, data: str):
        self.key = key
        self.data = data
        self.duplicates = 0

    @property
    def serialize(self) -> dict:
        return {
            'key': self.key,
            'data': json.loads(self.data),
            'duplicates': self.duplicates
        }

    def update_duplicates(self):
        self.duplicates += 1


def check_for_request_duplicates(key):
    session = Session()
    query = session.query(Request).filter(
        Request.key == key
    )
    return query.count()
