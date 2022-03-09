from django.db import models

class TeamMember(models.Model):
    first_name = models.CharField(max_length=126)
    last_name = models.CharField(max_length=126)
    story = models.TextField(max_length=1000)
    photo = models.ImageField(null = True)

    
    def __str__(self):
        return self.first_name