from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 400)

    def __str__(self):
        return self.name


class Grade(models.Model):
    type = models.CharField(max_length=1)

    def __str__(self):
        return self.type


class Certificate_Type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    class Meta:
        verbose_name_plural = "Faculty"
    name = models.CharField(max_length = 50)
          
    def __str__(self):
        return self.name
        

class Department(models.Model):
    name = models.CharField(max_length = 50)
    faculty = models.ForeignKey(Faculty, blank=True, null=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name

class Student(models.Model):
    school = models.ForeignKey(School, blank=True, null=True, on_delete=models.CASCADE)
    fullname = models.CharField(max_length = 200)
    year_of_graduation = models.IntegerField()
    department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, blank=True, null=True, on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(Certificate_Type, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname









