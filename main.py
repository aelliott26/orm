############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

from faker import Faker
from db.models import *
from gym_membership.models import *
from django.contrib.auth.models import User
import random
from model_bakery.recipe import Recipe


############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

"""
In case you need to start over. 
Note- this will delete any other tables on the public schema.
Alternatively, you could drop django's tables one-by-one

Login to psql and run these commands in order:

DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO postgres, public;

... then migrate again, and re-create your superuser
"""



fake = Faker()

MemLevels = [
    ("G", "Gold"),
    ("P", "Platinum"),
    ("S", "Silver"),
    ("B", "Bronze"),
]

PType = [
    ("CC", "Credit Card"),
    ("C", "Cash"),
    ("DC", "Debit Card"),
]

for i in range(40):
    a = Member(
        member_id=fake.random_int(min=0, max=40),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        phone_num=fake.phone_number(),
        birthday=fake.date_of_birth(),
        m_level=random.choice(MemLevels)
    )
    a.save()

    b = PersonalTrainer(
        trainer_id=fake.random_int(min=0, max=40),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
    	email=fake.email(),
        phone_num=fake.phone_number()
    )
    b.save()

    c = CheckIn(
        member=random.choice(list(Member.objects.all())),
        checkin_date=fake.date_time_this_year()
    )
    c.save()

    d = Class(
        class_id=fake.random_int(min=0, max=40),
        class_dt=fake.date_time_this_year(),
        trainer=random.choice(list(PersonalTrainer.objects.all())),
        description=" ".join(fake.sentences(2))
    )
    d.save()

    e = SignUp(
        member=random.choice(list(Member.objects.all())),
        class_instance=random.choice(list(Class.objects.all()))
    )
    e.save()

    f = Payment(
        payment_id=fake.random_int(min=0, max=40),
        member=random.choice(list(Member.objects.all())),
        amount=round(fake.pyfloat(left_digits=2, right_digits=2, positive=True), 2),
        payment_date=fake.date_time_this_year(),
        payment_type=random.choice(PType)
    )
    f.save()











