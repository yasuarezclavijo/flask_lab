from enum import auto
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey,  Integer, String, Table
from sqlalchemy.orm import relationship

Base = declarative_base()

class Pokemon(Base):
    __tablename__ = 'pokemon'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    photo = Column(String(255))