from django.db import models
gender=(
    ("male","Male"),
    ("female","Female"),
)
# Create your models here.
class Signup(models.Model):
    First_Name=models.CharField(max_length=100,default="")
    Last_Name=models.CharField(max_length=100,default="")
    Email=models.EmailField(max_length=100,default="")
    Password=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.First_Name



class Health_Professional_Account(models.Model):
    Health_Professional_Account_Id = models.AutoField(primary_key=True)
    Full_Name=models.CharField(max_length=100, default="")
    First_Name=models.CharField(max_length=100, default="")
    Last_Name=models.CharField(max_length=100, default="")
    Email=models.EmailField(max_length=100, default="")
    Username=models.CharField(max_length=100, default="")
    Gender=models.CharField(max_length=100, choices=gender,default="male")
    Date_of_Birth=models.DateField(blank=True, null=True)
    Password=models.TextField(max_length=3000, default=" ")
    Degree=models.CharField(max_length=200, default="")
    Affiliation=models.CharField(max_length=200, default="")
    Bio=models.TextField(default="")
    Street_Address=models.CharField(max_length=500, default="")
    City=models.CharField(max_length=500, default="")
    State=models.CharField(max_length=500, default="")
    Country=models.CharField(max_length=500, default="")
    Location=models.CharField(max_length=500, default="")
    Role=models.CharField(max_length=100,default="earhealthprofessional")
    Health_Professional_Image=models.ImageField(upload_to='Health_Professional/',default="dummy.jpg")
    
    
    def __str__(self):
        return self.Full_Name