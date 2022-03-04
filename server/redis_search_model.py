import os
from redisearch import Client, TextField, IndexDefinition
# from models import sess, Task


# Creating a client with a given index name
redis_search_client = Client("redis", host='redis')

# IndexDefinition is avaliable for RediSearch 2.0+
definition = IndexDefinition(prefix='doc:')

# Creating the index definition and schema
try:
    redis_search_client.create_index((TextField("title"), TextField("body")), definition=definition)
except:
    pass

