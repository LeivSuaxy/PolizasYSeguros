from django.db import models
from common.models.base import BaseModel

# Create your models here.
class Coverage(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

class CoverageRangeRelation(BaseModel):
    coverage = models.ForeignKey(Coverage, on_delete=models.CASCADE)
    range = models.ForeignKey('ranges.Range', on_delete=models.CASCADE)

    class Meta(BaseModel.Meta):
        unique_together = ('coverage', 'range')

    def __str__(self):
        return f'{self.coverage.name} - {self.range.type}'