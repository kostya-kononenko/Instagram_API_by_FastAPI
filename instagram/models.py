from sqlalchemy.sql.schema import ForeignKey
from database.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship


class DBPost(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('user.DBUser', back_populates='items')
