from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    lastname1 = models.CharField(max_length=45)
    lastname2 = models.CharField(max_length=45, null=True)
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=128)
    profile_picture = models.CharField(max_length=255, null=True)
    birthdate = models.DateField()
    creation_date = models.DateTimeField()
    update_date = models.DateTimeField(null=True)
    role = models.ForeignKey('User_role', on_delete=models.RESTRICT, db_column='role_id')

class User_role(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=45)