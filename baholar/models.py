from django.db import models

class Student(models.Model):
    first_name=models.CharField(max_length=100, null=False, blank=False)
    last_name=models.CharField(max_length=100, null=False, blank=False)
    birth_date=models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.first_name


class Subject(models.Model):
    name=models.CharField(max_length=100, null=False,blank=False)

    def __str__(self):
        return self .name


class Grade(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE, related_name="grades")
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    grade=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f" {self.student} - {self.subject} fandan - {self.grade}  baho olgan"
