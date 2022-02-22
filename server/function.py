from sqlalchemy import create_engine, Column, Integer, String, BOOLEAN, null
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import redis
from models import sess, Task,  Base, engine

Base.metadata.create_all(engine)   

def assigned_zero():
    data = sess.query(Task).filter(Task.assigned==None).count()
    if data:
        sess.query(Task).filter(Task.assigned==None).update(dict(assigned=0))
        sess.commit()
    sess.close()
    return data


def assigned_one():
    data = sess.query(Task).filter(Task.assigned==0).count()
    if data:
        sess.query(Task).filter(Task.assigned==0).update(dict(assigned=1))
        sess.commit()
    sess.close()
    return data