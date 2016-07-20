from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class Poketmon(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Capture(models.Model):
    user = models.ForeignKey(User)
    poketmon = models.ForeignKey(Poketmon)
    location = models.CharField(max_length=15)

    def __str__(self):
         return '{}이 {}에서 {}를 포획'.format(self.user.username, self.location, self.poketmon.name)
