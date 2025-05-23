from datetime import timedelta

broker_url='confluentKafka://localhost:9092'    # Kafka as message broker

accept_content = ['json']   # Accept only JSON-encoded messages
task_serializer = 'json'    # Use JSON to serialize task arguments
timezone='UTC'  # Scheduler runs tasks assuming UTC timezone

imports=('tasks.task',)     # Load task definitions from tasks/task.py 
task_default_queue='dummy_kafka_topic'      # All tasks go to this Kafka topic unless specified

# allowed tasks (security measure to limit what tasks can be executed)
celery_tasks = [
    'tasks.task.send_an_email'
]

# Defines periodic tasks (used with Celery Beat)
beat_schedule={
    'send-an-email-every-5-minutes': {
        'task': 'tasks.task.send_an_email',
        'schedule': timedelta(minutes=5),
    }
}