from database.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class DBUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship('instagram.DBPost', back_populates='user')
