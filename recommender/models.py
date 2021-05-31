from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.username, filename)

class Student(models.Model):
    username=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=40,null=True)
    topics_of_interest=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    course_name=models.CharField(max_length=200,null=True)
    category=models.CharField(max_length=200,null=True)
    course_provider=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.course_name

class Chapter(models.Model):
    course_id= models.ForeignKey(Course, on_delete=models.CASCADE)
    assignment_que=models.CharField(max_length=400,null=True)
    upload_assignment=models.FileField(upload_to = user_directory_path,null = True)

class Rating(models.Model):
    student_id= models.ForeignKey(Student, on_delete=models.CASCADE,related_name='student')
    course_id= models.ForeignKey(Course, on_delete=models.CASCADE,related_name='course')
    #rating=models.IntegerField(null=True)
    TYPE_SELECT = (
        ('1', 'Like'),
        ('-1', 'Dislike'),
    )
    rating= models.IntegerField(choices=TYPE_SELECT,null=True)



