import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')

import django 
django.setup()

from apptwo.models import User
from faker import Faker

fake_generator = Faker()

def populate_users(count=20):
    for user in range(count):
        first_name = fake_generator.first_name()
        last_name = fake_generator.last_name()
        email = fake_generator.email()
        user_record = User.objects.get_or_create(first_name=first_name,last_name=last_name,email=email)

if __name__ == "__main__":
    print("Starting the fake users population")
    populate_users(25)
    print("Population completed look into server admin for all fields !!")
        

