# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from time import time
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50,null=False)
    email = models.EmailField( max_length=254,null=False)
    message = models.TextField(null=False)
    createdAt = models.DateTimeField( default=timezone.now)

    def __str__(self):
        return f"Message from {self.name}"

