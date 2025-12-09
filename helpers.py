import random
import string

import requests

from urls import *


def generate_email():
    random_string = ''.join(random.choices(string.ascii_lowercase, k=10))
    random_domain = ''.join(random.choices(string.ascii_lowercase, k=5))
    random_tld = random.choice(['com', 'net', 'org'])
    email = f"{random_string}@{random_domain}.{random_tld}"
    return email

def generate_password():
    password = ''.join(random.choices(string.ascii_lowercase, k=10))
    return password

def create_user(payload):
    return requests.post(f'{BASE_URL}{CREATE_USER}', data=payload)

def delete_user(access_token):
    return requests.delete(f'{BASE_URL}{EDIT_GET_DELETE_USER}', headers={"Authorization": f"{access_token}"})