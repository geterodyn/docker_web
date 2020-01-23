from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()

class DivisionResult(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), unique=True, nullable=False)
    top = Column(Integer)
    bottom = Column(Integer)
    answer = Column(Float, nullable=True)
    created = Column(DateTime(timezone=False), default=func.now())

    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def __str__(self):
        return f"({self.top},{self.bottom})"

