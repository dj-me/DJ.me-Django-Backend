from django.db import models

# Create your models here.

class user(models.Model):
    hostname = models.CharField(max_length = 250 , default = 'NULL')
    hotspot = models.CharField(max_length = 250 , default = 'NULL')
    access_token = models.CharField(max_length = 250 , default = 'NULL')
    playid = models.CharField(max_length = 250 , default = 'NULL')
    playurl = models.CharField(max_length = 250 , default = 'NULplayL')

    def __str__(self):
        return self.hostname

class djsessions(models.Model):
    hostedsession=models.CharField(max_length = 250 , default = 'NULL')
    hostname = models.ForeignKey(user, on_delete=models.CASCADE)
    member = models.CharField(max_length = 250 , default = 'NULL')
  
    def __str__(self):
        return self.hostedsession

class finalplaylist(models.Model):
    hostname = models.ForeignKey(user, on_delete=models.CASCADE)
    hostedsession = models.ForeignKey(djsessions, on_delete=models.CASCADE)
    pid = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.pid


class hostsong(models.Model):
    hostedsession = models.ForeignKey(djsessions, on_delete=models.CASCADE)
    song = models.CharField(max_length = 250 , default = 'NULL')
    counter = models.CharField(max_length = 250 , default = '0')

    def __str__(self):
        return self.song