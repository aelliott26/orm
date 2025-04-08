import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
import django
django.setup()

from faker import Faker
from gym_membership.models import *
from django.contrib.auth.models import User
import random

