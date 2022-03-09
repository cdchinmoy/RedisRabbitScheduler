import redis
from sqlalchemy import true
redis_client = redis.Redis(host='redis', port=6379)

def key_exist(search_key):  
    key_list = []  
    for key in redis_client.scan_iter(search_key):
        key_list.append(key)   
    if len(key_list) > 0:
        return True
    else:
        return False

def insert_to_redis(table_prefix, kwargs):
    for row in kwargs:
        for key, value in row.items():
            redis_client.hset(str(table_prefix)+str(row['id']), key, str(value))

def update_redis(table_prefix, kwargs):
    for row in kwargs:   
        for key, value in row.items():
            redis_client.hset(str(table_prefix)+str(row['id']), key, str(value))

    
def get_data_from_redis(search_key, search_field, search_value):
    response = []
    for key in redis_client.scan_iter(search_key):
        row = redis_client.hgetall(key)
        data = decode_object(row)
        if search_field in data.keys():
            if data[search_field] == search_value:
                response.append(data)

    return response

def decode_object(data):
    res = {}
    for key, val in data.items():
        key = decode_string(key)
        val = decode_string(val)
        res[key] = val
    return res

def decode_string(data):
    return data.decode('utf-8')