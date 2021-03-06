from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Constraint, PrimaryKeyConstraint, ForeignKeyConstraint, Text


class BaseUser(Base):
    """docstring for BaseUSer."""
    __tablename__ = 'baseuser'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    email = Column(String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name
