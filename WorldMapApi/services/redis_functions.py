import redis
#Parameters
HOST = 'localhost'
PASSWORD = 'eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81'
PORT = 6379

try:
    #Connect to Redis
    redis_client = redis.StrictRedis(host = HOST, port = PORT, password = PASSWORD)          
except Exception as e:
    print('Error connecting to Redis\n ' + str(e))
    exit()
    

def send_data_to_redis(key, value):
    try:
        redis_client.set(key, value)
    except Exception as e:
        print('Error in send_data_to_redis function: ' + str(e))
        exit()  