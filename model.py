from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker 
from sqlalchemy import create_engine

Base = declarative_base()

class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key = True)
    content= Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    topic = Column(String)
    
def __repr__(self):
    return ("article title: {}, article content:{}".format(self.title, self.content))

class User(Base):
  __tablename__="user"
  id=Column(Integer, primary_key=True)
  name=Column(String, unique=True )
  password=Column(String)
 
  def __repr__(self):
    return ("user name:{}, user password:{}".format(self.name, self.password))