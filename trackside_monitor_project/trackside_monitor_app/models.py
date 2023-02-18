from django.db import models


class LoraThread(models.Model):
    thread_name = models.CharField(max_length=10)
    thread_flag = models.BooleanField()
