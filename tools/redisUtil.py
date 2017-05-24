import redis
r = redis.Redis(host='104.140.18.185',port=6379,db=0)
print(r.info)
print(r.dbsize())

