from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from model_utils.models import TimeStampedModel

# Create your models here.

class Status(models.TextChoices):
    UNSTATED = 'u', "Not started yet"
    ONGOING = 'o',"Ongoing"
    FINISHED = 'f',"Finished"

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Task name",max_length=65,unique=True)
    status = models.CharField(verbose_name="Task status",max_length=1,choices=Status.choices)


    class Meta:
        verbose_name = "任務"
        db_table = "Task"

    def __str__(self):
        return self.name

class Entry(TimeStampedModel, MPTTModel):
    title = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['created']