from django.db import models

class TeamMembers(models.Model):
    first_name = models.CharField(max_length=126)
    last_name = models.CharField(max_length=126)
    story = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.first_name