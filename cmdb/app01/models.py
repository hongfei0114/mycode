from django.db import models

# Create your models here.



class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.name
    

class Service(models.Model):
    name = models.CharField(max_length=32)
    Users = models.ForeignKey(to='User',)


class Hosts(models.Model):
    name = models.CharField(max_length=32)
    host_pass = models.CharField(max_length=32)
    services = models.ManyToManyField(to='Service',related_name='hosts')
