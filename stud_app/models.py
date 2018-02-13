from django.db import models
from django.utils import timezone

# Create your models here.
class School(models.Model):

    rating=(
        ('one','1'),
        ('two','2'),
        ('three','3'),
        ('four','4'),
        ('five','5'),
    )
    
    name = models.CharField(max_length = 50)
    address = models.TextField(null = True, blank = True)
    rating = models.CharField(max_length=50, choices=rating)
    email = models.EmailField()
    contact = models.IntegerField(null = True, blank = True)
    website = models.CharField(max_length=50, null = True, blank = True)
    is_enabled = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    
    
    
    def __str__(self):
		return self.email 


class Student(models.Model):
    standard=(
		('FIve','5'),
		('six','6'),
		('seven','7'),
		('eight','8'),
		('nine','9'),
		('ten','10'),
    )
    
    
    school = models.ForeignKey(School)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    residence_address = models.TextField(null=True, blank=True)
    standard = models.CharField(max_length=50, choices=standard)
    roll_no = models.IntegerField()
    fees = models.CharField(max_length=50)
    is_enabled = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.school.email + '-' + str(self.roll_no)