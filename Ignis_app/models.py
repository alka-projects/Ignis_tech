from django.db import models

# Create your models here.
class event(models.Model):
    # ‘event_name’, ’data’ ,’time’, ‘location’ ,’image’, ‘is_liked’
    event_name=models.CharField(max_length=30)
    date=models.DateField(max_length=30)
    time=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    image=models.ImageField(upload_to='images/')
    is_liked=models.BooleanField(default=False)
