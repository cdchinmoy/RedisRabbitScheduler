from sys import implementation
from sqlalchemy import create_engine, Column, Integer, String, BOOLEAN, null
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import redis
from models import sess, Task
from redis_search_model import redis_search_client
from redis_core import  key_exist


def assigned_zero():
        
    search_keyword = "job:*"
    if key_exist(search_keyword):

        res = redis_search_client.search("@assigned:none")
        if len(res.docs):

            for row in res.docs:
                redis_search_client.redis.hset('job:'+str(row.id),
                                mapping={
                                    'assigned': int(0)
                                })


            sess.query(Task).filter(Task.id==row.id).update(dict(assigned=0))
            sess.commit()
            sess.close()
            return len(res.docs)

    else:

        data = sess.query(Task).filter(Task.assigned==None).count()
        if data:
            sess.query(Task).filter(Task.assigned==None).update(dict(assigned=0))
            sess.commit()
            sess.close()


        rows = sess.query(Task).all()
        if rows:
            for row in rows:

                if row.assigned == None:
                    assigned = 'none'
                else:
                    assigned = int(row.assigned)
                redis_search_client.redis.hset('job:'+str(row.id),
                            mapping={
                                'id': row.id,
                                'name':row.name,
                                'assigned': assigned
                            })


        return data           

    


def assigned_one():
    data = sess.query(Task).filter(Task.assigned==0).count()
    if data:
        sess.query(Task).filter(Task.assigned==0).update(dict(assigned=1))
        sess.commit()
    sess.close()
    return 2