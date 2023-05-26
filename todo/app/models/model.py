from sqlalchemy import Column, Integer, String, ForeignKey
from app.routers.db import Base


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
