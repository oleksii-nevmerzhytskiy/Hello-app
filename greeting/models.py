from django.db import models

class ContactModel(models.Model):
	name = models.CharField(max_length=30)

