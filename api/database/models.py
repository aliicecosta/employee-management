from sqlalchemy import Column, Float, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"

    registration = Column(Integer, primary_key=True)
    name = Column(String(30))
    surname = Column(String)
    role = Column(String(10))
    leader = Column(String(30))
    salary = Column(Float)
    password = Column(String(20))
    status = Column(Boolean)

