from sys import implementation
from models import sess, Task
from redis_core import  key_exist, insert_to_redis, get_data_from_redis, update_redis

def assigned_zero():
    search_keyword = "job:*"
    if key_exist(search_keyword):
        res = get_data_from_redis(search_keyword, "assigned", "none")
        if len(res):
            args = []
            kwargs = []
            for row in res:
                args.append(row['id'])
                row_dict = {}
                row_dict['assigned'] = 0
                kwargs.append(row_dict)
            #DATABASE REDIS
            update_redis(search_keyword, args, kwargs)
            #DATABASE UPDATE
            update_data = {'assigned':0}
            update_database(res, update_data)
            return len(res)  
        else:
            return 0    
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
                args = []
                kwargs = []
                for row in rows:
                    args.append(row.id)
                    data_dict = vars(row)
                    if '_sa_instance_state' in data_dict:
                        del data_dict['_sa_instance_state']
                    kwargs.append(data_dict)
                search_keyword = "job:*"
                insert_to_redis(search_keyword, args, kwargs)
        return data


def assigned_one():
    search_keyword = "job:*"
    res = get_data_from_redis(search_keyword, "assigned", "0")
    if len(res):
        args = []
        kwargs = []
        for row in res:
            args.append(row['id'])
            row_dict = {}
            row_dict['assigned'] = 1
            kwargs.append(row_dict)
        #DATABASE REDIS
        update_redis(search_keyword, args, kwargs)
        #DATABASE UPDATE
        update_data = {'assigned':1}
        update_database(res, update_data)
        return len(res)  
    else:
        return 0    
    

def update_database(data, update_data):
    for row in data:
        sess.query(Task).filter(Task.id==row['id']).update(update_data)
        sess.commit()
        sess.close()       