from django.db import models
from common.models.base import BaseModel

# Create your models here.
class Poliza(BaseModel):
    active = models.BooleanField(default=False)
    init_date = models.DateField()
    end_date = models.DateField()
    client = models.ForeignKey('authentication.ModifiedUser', on_delete=models.CASCADE, related_name='client_policies')
    worker = models.ForeignKey('authentication.ModifiedUser', on_delete=models.CASCADE, related_name='worker_policies')
    type = models.CharField(max_length=255)
    description = models.TextField()


