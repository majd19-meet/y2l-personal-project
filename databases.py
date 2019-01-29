from model import Base, Article, User   
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///projects.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(content, user_id, topic):
    print("Added an article!")
    article = Article(content=content, user_id=user_id, topic=topic)
    session.add(article)
    session.commit()

def get_all_articles():
  articles = session.query(Article).all()
  return articles

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

def query_by_topic(topic):
  results= session.query(Article).filter_by(topic=topic).all()
  return results

def delete_by_topic(topic):
  session.query(Article).filter_by(topic=topic).delete()
  session.commit()

# delete_by_topic("death")