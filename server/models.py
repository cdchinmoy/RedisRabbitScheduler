from sqlalchemy import create_engine, Column, Integer, String, BOOLEAN, null
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

def db_string(db_user, db_pass, db_host, db_name):
    return 'mysql://%s:%s@%s/%s?charset=utf8mb4' % (db_user, db_pass, db_host, db_name)

engine = create_engine(db_string(os.environ['DB_USER'],os.environ['DB_PASS'],os.environ['DB_HOST'],os.environ['DB_NAME']))
Session = sessionmaker(bind=engine)
sess = Session()

Base = declarative_base()

class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key = True)
    name = Column(String(250))
    assigned = Column(BOOLEAN)
 
    def __init__(self, name, assigned):
        self.name = name
        self.assigned = assigned

Base.metadata.create_all(engine)   