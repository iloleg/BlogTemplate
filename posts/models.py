from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_subtitle = models.CharField(max_length=120, blank=True, default='')
    post_body = models.TextField()
    post_created_on = models.DateTimeField(default=now)
    
    

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('post_detail', args=[(self.id)])
    
