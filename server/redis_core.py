import redis
redis_client = redis.Redis(host='redis', port=6379)

def key_exist(search_key):  
    key_list = []  
    for key in redis_client.scan_iter(search_key):
        key_list.append(key)   
    if len(key_list) > 0:
        return True
    else:
        return False