from django.db import models

# Create your models here.

class user(models.Model):
    hostname = models.CharField(max_length = 250 , default = 'NULL')
    hotspot = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.hostname

class hostsong(models.Model):
    hostname = models.ForeignKey(user, on_delete=models.CASCADE)
    song = models.CharField(max_length = 250 , default = 'NULL')
    counter = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.song


class djsessions(models.Model):
    hostname = models.ForeignKey(user, on_delete=models.CASCADE)
    member = models.CharField(max_length = 250 , default = 'NULL')
  
    def __str__(self):
        return self.member

class finalplaylist(models.Model):
    hostname = models.ForeignKey(user, on_delete=models.CASCADE)
    hostedsession = models.CharField(max_length = 250 , default = 'NULL')
    counter = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.song
