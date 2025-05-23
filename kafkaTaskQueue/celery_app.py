from celery import Celery
from kafkaTaskQueue import celery_config

# Initialize the Celery application with the configuration from celery_config
celery_app = Celery()
celery_app.config_from_object(celery_config)

# Start the Celery application
if __name__ == "__main__":
    celery_app.start()

