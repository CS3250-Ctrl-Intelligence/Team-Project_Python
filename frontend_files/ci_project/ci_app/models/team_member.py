from django.db import models

class TeamMember(models.Model):
    first_name = models.CharField(max_length=126)
    last_name = models.CharField(max_length=126)
    story = models.TextField(max_length=1000)
    photo = models.ImageField(null = True, blank = True)

    
    def __str__(self):
        return self.first_name


    # property decorator is added to access photo.url like an attribute
    @property
    def photoURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url