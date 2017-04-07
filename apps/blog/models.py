from __future__ import unicode_literals
from django.db import models

class  Blog(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    entry = models.TextField(max_length = 4000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
