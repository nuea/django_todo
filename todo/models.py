from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=80, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    price = models.IntegerField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str___(self):
        return self.title