import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import user
from faker import Faker

fake = Faker()
topics =['FirstName',"Lastname","Email"]

def populate(N=5):
    for entry in range(N):
        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_email = fake.email()

        usr = user.objects.get_or_create(FirstName=fake_first_name,SecondName=fake_last_name,email=fake_email)

if __name__ =="__main__":
    print("Populating the databases.....Please wait")
    populate(20)
    print("populating complete")
