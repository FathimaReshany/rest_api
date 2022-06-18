from django.db import models

# Create your models here.

class Users(models.Model):
    emp_id=models.CharField(max_length=50, unique=True)
    name= models.CharField(max_length=100)
    age=models.IntegerField()

    def upload_photo(selfself,filename):
        path='Employees/hrm/photo/{}'.format(filename)
        return path

    image=models.ImageField(upload_to=upload_photo, null=True, blank= True)

    def upload_file(selfself, filename):
        path = 'Employees/hrm/file/{}'.format(filename)
        return path

    resume = models.FileField(upload_to=upload_file, null=True, blank=True)


    def __str__(self):
        return f"{self.emp_id} - {self.name}"
