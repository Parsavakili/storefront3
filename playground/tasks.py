from time import sleep
from celery import shared_task

print('before entering to func')  
# Configure logging to provide more context and details
@shared_task
def notify_customers(message):
    print('Starting to send emails...')
    print('sending 10k emails..') 
    print(message) 
    sleep(10) 
    print('Emails were successfully sent!')