from django.db import models
from common.models.base import BaseModel
from ranges.enum.ranges import Ranges

# Create your models here.
class Range(BaseModel):
    type = models.CharField(max_length=20, choices=[(range.value, range.name) for range in Ranges])
    poliza = models.ForeignKey('poliza.Poliza', on_delete=models.CASCADE)
    price = models.FloatField()
    duration = models.IntegerField(help_text='Duration of the poliza')