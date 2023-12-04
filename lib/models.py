import os
import sys

sys.path.append(os.getcwd())

from datetime import datetime

from sqlalchemy import create_engine, desc
from sqlalchemy import (
    CheckConstraint, UniqueConstraint,
    Column, DateTime, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///migrations_test.db')

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), index=True)
    email = Column(String(55))
    class_level = Column(Integer())  # Renamed 'grade' to 'class_level'
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"Student {self.id}: " \
               + f"{self.name}, " \
               + f"Class Level {self.class_level}"  # Updated repr to use 'class_level'
