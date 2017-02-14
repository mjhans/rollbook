from django.db import models
from django.utils import timezone

class Person(models.Model):
	person_name = models.TextField()
	person_type = models.IntegerField()
	created_date = models.DateTimeField(
		default=timezone.now)

	def register(self):
		self.save()

	def __str__(self):
		return self.person_name