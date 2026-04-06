from fastapi import FastAPI, HTTPException, Query
from redis import Redis
from rq import Queue
from .worker import process_query

app = FastAPI()

redis_conn = Redis()
queue = Queue(connection=redis_conn)

@app.get('/')
def root():
    return {"status": 'server is up & running'}

@app.post('/chat')
def chat(
        query: str = Query(..., description="The chat query of user")
):
    job = queue.enqueue(process_query, query)

    return {"status": "queued", "job_id": job.id}

@app.get('/job-status')
def get_result(
    job_id: str = Query(..., description="The job id")
):
    result = job.return_value()
    return {"result", result}

