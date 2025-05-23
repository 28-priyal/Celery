from redisTaskQueue.celery_app import celery_app

# This is a simple Celery task that simulates sending an email.
# In a real-world scenario, you would replace this with actual email sending logic.
@celery_app.task
def send_an_email():
    # Simulate sending an email
    print("Email sent")
