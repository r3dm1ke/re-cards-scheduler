import requests
import schedule
import time
import os

NOTIFICATION_FUNCTION_URL = 'https://us-central1-re-cards-prod.cloudfunctions.net/reminder'


def send_notification_request():
    token = os.environ['FIREBASE_FUNCTIONS_TOKEN']
    headers = {'Authorization': token}
    response = requests.post(NOTIFICATION_FUNCTION_URL, headers=headers)
    print(f'Got response! Status: {response.status_code}, content: {response.content()}')


def schedule_notification_request():
    schedule.every(30).minutes.do(send_notification_request)


def loop():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    loop()
