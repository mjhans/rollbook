from mongoengine import *
from django.db import models
from django.utils import timezone

connect('testdb', host='127.0.0.1', port=27027)

class Person(Document):
	person_name = StringField()
	person_type = IntField()
	created_date = DateTimeField(default=timezone.now)

	def __init__(self):
		pass

	def register(self):
		self.save()

	def __str__(self):
		return self.person_name