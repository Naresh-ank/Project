from django.db import models

class User_Registration(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=30)
    address = models.TextField(max_length=300)
    contact = models.IntegerField()
    date_of_birth = models.DateField()
    nominee = models.CharField(max_length=30)

class Take_Insurance(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=30,primary_key=True)
    policy_type = models.CharField(max_length=30)
    policy_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    policy_duration = models.IntegerField()
    policy_taking_date = models.DateField()
    premium_amount = models.DecimalField(max_digits=10,decimal_places=2)
    benificial_amount = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField(max_length=100)

class Pay_Premium(models.Model):
    policy_holder_name = models.CharField(max_length=30,primary_key=True)
    policy_payment_date = models.DateField()
    premium_amount = models.DecimalField(max_digits=10,decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10,decimal_places=2)
    policy_number = models.IntegerField()
    dd_no = models.IntegerField()