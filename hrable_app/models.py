from django.db import models


class HR(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    joining_date = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    private_key = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    private_key = models.CharField(max_length=100)
    joining_date = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

class Admin(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    private_key = models.CharField(max_length=100)

class Jobs(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    requirements = models.CharField(max_length=1000)
    salary = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    startdate = models.CharField(max_length=100)
    enddate = models.CharField(max_length=100)
    jobtype = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

class Job_Application(models.Model):
    jobname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    job_id = models.CharField(max_length=100)
    cover_letter = models.CharField(max_length=10000)
    status = models.CharField(max_length=100, default="Pending")
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    gender = models.CharField(max_length = 100)



class Refferal(models.Model):
    job_id = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    name_of_referrer = models.CharField(max_length=100)

class Quote(models.Model):
    quote = models.CharField(max_length=5000)

class Time(models.Model):
    username = models.CharField(max_length=100)
    checkin = models.CharField(max_length=100)
    checkout = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    userid = models.CharField(max_length=100)

class Query(models.Model):
    empname = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=100)
    query_type = models.CharField(max_length=1000)
    query = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default="Pending")
    hr_acknowledging = models.CharField(max_length=100, default="Pending")
    hr_id = models.CharField(max_length=100,default="Pending")
    hr_comment = models.CharField(max_length=100,default="Pending")