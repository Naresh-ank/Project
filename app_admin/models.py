from django.db import models

class Login(models.Model):
    username = models.CharField(primary_key=True,max_length=30)
    password = models.CharField(max_length=10)
    usertype = models.CharField(max_length=20)

class Employee(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    contact = models.IntegerField()
    address = models.TextField(max_length=300)
    department_id = models.IntegerField()

class Life_Policy(models.Model):
    policy_type = models.CharField(max_length=30)
    policy_name = models.CharField(max_length=30,primary_key=True)
    description = models.TextField(max_length=100)
    time_duration = models.IntegerField()
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    premium_amount = models.DecimalField(max_digits=10,decimal_places=2)
    premium_number = models.IntegerField()
    rate_of_interest = models.DecimalField(max_digits=10,decimal_places=2)
    rules = models.TextField(max_length=100)
    benificial_amount = models.DecimalField(max_digits=10,decimal_places=2)
    accidential_benifit = models.DecimalField(max_digits=10,decimal_places=2)

class Health_Policy(models.Model):
    policy_type = models.CharField(max_length=30)
    policy_name = models.CharField(max_length=30,primary_key=True)
    description = models.TextField(max_length=100)
    time_duration = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)
    premium_number = models.IntegerField()
    coverage_amount = models.DecimalField(max_digits=10, decimal_places=2)
    marital_status = models.CharField(max_length=20)
    no_of_family = models.IntegerField()

class Car_Policy(models.Model):
    policy_type = models.CharField(max_length=30)
    policy_name = models.CharField(max_length=30,primary_key=True)
    description = models.TextField(max_length=100)
    time_duration = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)
    premium_number = models.IntegerField()
    rate_of_interest = models.DecimalField(max_digits=10, decimal_places=2)
    rules = models.TextField(max_length=100)
    benificial_amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=30)
    vehicle_no = models.IntegerField()
    company = models.CharField(max_length=30)
    model = models.CharField(max_length=30)

class Home_Policy(models.Model):
    policy_type = models.CharField(max_length=30)
    policy_name = models.CharField(max_length=30,primary_key=True)
    description = models.TextField(max_length=100)
    time_duration = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)
    premium_number = models.IntegerField()
    rate_of_interest = models.DecimalField(max_digits=10, decimal_places=2)
    rules = models.TextField(max_length=100)
    benificial_amount = models.DecimalField(max_digits=10, decimal_places=2)
    property_cost = models.DecimalField(max_digits=10, decimal_places=2)


