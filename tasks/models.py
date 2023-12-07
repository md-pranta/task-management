from django.db import models
from categories.models import Category
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_completed = models.BooleanField(default = False)
    date = models.DateField()
    
    category = models.ManyToManyField(Category)
    
    
    def __str__(self) -> str:
        return self.title