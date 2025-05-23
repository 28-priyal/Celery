from celery.schedules import timedelta
import os

def get_broker_url():
    # Redis configuration
    redis_host = os.environ.get("REDIS_HOST", "localhost")
    redis_port = int(os.environ.get("REDIS_PORT", 6379))
    redis_db = int(os.environ.get("REDIS_DB", 0))
    broker_url = f"redis://{redis_host}:{redis_port}/{redis_db}"
    return broker_url

broker_url=get_broker_url()

task_ignore_result=True
accept_content=['json']
result_serializer='json'
task_serializer='json'
timezone='UTC'
imports=('tasks.task',)
task_default_queue='dummy_redis_queue' 

celery_allowlist_tasks = [
    'tasks.task.send_an_email'
]

beat_schedule={
    'send-an-email-every-5-minutes': {
        'task': 'tasks.task.send_an_email',
        'schedule': timedelta(minutes=5),
    }
}