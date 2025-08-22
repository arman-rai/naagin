#!/usr/bin/env python3

import random,secrets, string 
from datetime import datetime

print(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Password: ", generate_password())

