from models import sess, Task
from redis_core import  key_exist, insert_to_redis, get_data_from_redis, update_redis

def assigned_zero():
    search_keyword = "job:*"
    if key_exist(search_keyword):
        res = get_data_from_redis(search_keyword, "assigned", "none")
        if len(res) > 0:
            kwargs = []
            for row in res:
                row_dict = {}
                row_dict['id'] = row['id']
                row_dict['assigned'] = False
                kwargs.append(row_dict)
            #DATABASE REDIS
            update_redis(search_keyword, kwargs)
            #DATABASE UPDATE
            update_data = {'assigned': False}
            update_database(res, update_data)
            return len(res)  
        else: 
            return 0    
    else:
        data = sess.query(Task).filter(Task.assigned==None).count()
        if data:
            sess.query(Task).filter(Task.assigned==None).update(dict(assigned=False))
            sess.commit()
            sess.close()
            task_count = data
        else:
            task_count = 0    

        rows = sess.query(Task).all()
        if rows:
            for row in rows:
                kwargs = []
                for row in rows:
                    data_dict = vars(row)
                    if '_sa_instance_state' in data_dict:
                        del data_dict['_sa_instance_state']
                    kwargs.append(data_dict)
                search_keyword = "job:*"
                insert_to_redis(search_keyword, kwargs)       
        return task_count


def assigned_one():
    search_keyword = "job:*"
    res = get_data_from_redis(search_keyword, "assigned", "False")
    if len(res) > 0:
        kwargs = []
        for row in res:
            row_dict = {}
            row_dict['id'] = row['id']
            row_dict['assigned'] = True
            kwargs.append(row_dict)
        #DATABASE REDIS
        update_redis(search_keyword, kwargs)
        #DATABASE UPDATE
        update_data = {'assigned': True}
        update_database(res, update_data)
        return len(res)  
    else:
        return len(res) 
    

def update_database(data, update_data):
    for row in data:
        sess.query(Task).filter(Task.id==row['id']).update(update_data)
        sess.commit()
        sess.close()       