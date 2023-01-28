import requests
import os
import glob
import re
import docx

from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from datetimerange import DateTimeRange
from os.path import join, dirname
from dotenv import load_dotenv
from termcolor import colored

DOTENV_PATH = join(dirname(__file__), '.env')
load_dotenv(DOTENV_PATH)

API_URL_BASE = 'https://api.linkedin.com/v2/'
AUTHOR = f"urn:li:person:{os.getenv('URN')}"
HEADERS = {
    'X-Restli-Protocol-Version': '2.0.0',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv("ACCESS_TOKEN")}'
}

def send_to_linkedin_api(current_document_text):
    api_url = f'{API_URL_BASE}ugcPosts'

    post_data = {
        "author": AUTHOR,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": current_document_text
                },
                "shareMediaCategory": "NONE"
            },
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "CONNECTIONS"
        },
    }

    response = requests.post(api_url, headers=HEADERS, json=post_data)

    if response.status_code == 201:
        print(" Le post a été envoyé sur LinkedIn.")
        print(response.content)
    else:
        print("\033[1;31;40m Erreur : ")
        print(response.content)

def get_document(filename):
    doc = docx.Document(filename)
    fullText = []
    for element in doc.paragraphs:
        fullText.append(element.text)

    return '\n'.join(fullText)

def check_documents_every_hour():
    documents_in_repertory = glob.glob("./scheduled_posts/*.docx")
    current_date_minus_one_hour = datetime.today() - timedelta(hours=1)
    current_date_plus_one_hour = datetime.today() + timedelta(hours=1)

    for key, filename in enumerate(documents_in_repertory):
        cleaned_filename = re.sub(r'^.*?___', '', filename).split('.docx')[0].split('__')
        
        date = cleaned_filename[0].split('_')
        date_day = int(date[0]) 
        date_month = int(date[1])
        date_year = int(date[2])

        time = cleaned_filename[1].split('_')
        time_hour = int(time[0])
        time_minute = int(time[1])

        scheduled_document_date = datetime(date_year, date_month, date_day, time_hour, time_minute)

        time_range = DateTimeRange(current_date_minus_one_hour, current_date_plus_one_hour)

        if scheduled_document_date in time_range:
            current_document_text = get_document(filename)
            send_to_linkedin_api(current_document_text)

def send_test():
    print(colored("\n Un document dans ./scheduled_posts,", "red"))
    print(colored(" A la date et l'heure d'aujourd'hui, doit être présent pour ce test.", "yellow"))

    check_documents_every_hour()

def init():
    print(colored(" Automatisation lancée ...", "yellow"))
    print(colored(" Ne fermez pas ce terminal.", "yellow"))

    scheduler = BlockingScheduler()
    scheduler.add_job(check_documents_every_hour, 'interval', hours=1)
    scheduler.start()
