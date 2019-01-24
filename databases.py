from model import Base, User     
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(name, password):
    print("Added a user!")
    user = User(name=name, password=password)
    session.add(user)
    session.commit()

def get_all_users():
  users = session.query(User).all()
  return users


def query_by_username(name):
  users= session.query(
    User).filter_by(
    name=name).first()
  return users 

def query_by_password(password):
  users= session.query(
    User).filter_by(
    password=password).all()
  return users   