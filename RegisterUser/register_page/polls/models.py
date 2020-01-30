from django.db import models

class Registration(models.Model):

    user_name = models.CharField(max_length=15)
    email_id = models.EmailField()
    password = models.CharField(max_length=15)
    conform_password = models.CharField(max_length=15)