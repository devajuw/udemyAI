from redis import redis
from rq import Queue

queue = Queue(connection= redis(
    host="localhost",
    port="6379"
))

queue.enqueue
