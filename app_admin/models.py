from django.db import models

# Create your models here.
class admin_tb(models.Model):
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    
class hobby_name_tb(models.Model):
    hobby_name=models.CharField(max_length=20)

class hobby_factor_tb(models.Model):
    factor_name=models.CharField(max_length=20)
    hobby_id=models.ForeignKey(hobby_name_tb,on_delete=models.CASCADE)

class season_tb(models.Model):
    season_name=models.CharField(max_length=20)

class season_factor_tb(models.Model):
    factor_name=models.CharField(max_length=20)
    season_id=models.ForeignKey(season_tb,on_delete=models.CASCADE)

class security_question_tb(models.Model):
    question=models.CharField(max_length=20)

class agefactor_tb(models.Model):
    min_age=models.IntegerField()
    max_age=models.IntegerField()
    factor_name=models.CharField(max_length=20)