from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Hotel(Base):
    __tablename__ = 'hotels'
    
    id = Column(Integer, primary_key=True)
    country = Column(String)
    title = Column(String)
    img_src_list = Column(String)
    rating = Column(Float)
    room = Column(String)
    price = Column(Float)
    location = Column(String)