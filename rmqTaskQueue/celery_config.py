from datetime import timedelta
from kombu.common import Exchange, Queue

broker_url='amqp://localhost:5672'  # URL for RabbitMQ broker (AMQP protocol)

accept_content=['json'] # Accept only JSON-encoded messages
task_serializer='json'  # Use JSON to serialize task arguments  
timezone='UTC'  # Scheduler runs tasks assuming UTC timezone

imports=('tasks.task',)  # Load task definitions from tasks/task.py 

# Define task queues with their associated exchange and routing key.
task_queues = (
    Queue('dummy_rmq_queue', Exchange('dummy_rmq_exchange'),
          routing_key='dummy_rmq_routing'),
)

# allowed tasks (security measure to limit what tasks can be executed)
celery_allowlist_tasks = [
    'tasks.task.send_an_email'
]

# Defines periodic tasks (used with Celery Beat)
beat_schedule={
    'send-an-email-every-5-minutes': {
        'task': 'tasks.task.send_an_email',
        'schedule': timedelta(minutes=5),
    }
}