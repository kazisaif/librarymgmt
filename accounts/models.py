from django.db import models

from django import forms

from django.contrib.auth.models import User
from sqlalchemy import true

# Create your models here.
class UserInfoForm(User):
    age=models.DateField()
    gender=models.CharField(max_length=30)
    contact=models.BigIntegerField()
    address=models.CharField(max_length=300,default="ABC")
    
    class Meta:
        db_table="UserInfoForm"


class LoginForm(forms.Form):
    #username=forms.CharField(max_length=30)
    email=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30,widget=forms.PasswordInput)

class books(models.Model):
    bookid=models.CharField(max_length=30)
    bookname=models.CharField(max_length=30)
    book_author=models.CharField(max_length=50)
    book_description=models.CharField(max_length=1000,null=True)
    publish_date=models.DateField(max_length=50,default="2022-02-24")
    book_image=models.ImageField(upload_to="media")

    def booki(self):
            return bookissue.objects.filter(book=self)

    class Meta:
        db_table='books'

    def __str__(self):
        return self.bookid
'''
class bookissue(models.Model):
    bookid=models.CharField(max_length=30)
    bookname=models.CharField(max_length=50)
    book_author=models.CharField(max_length=50)
    publish_date=models.DateField(max_length=50,default="2022-02-24")
    issuedate=models.DateField(max_length=20,null=True)
    returndate=models.DateField(max_length=20,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table='bookissue'

    def __str__(self):
        return self.bookid
'''
class bookissue(models.Model):
    #bookid=models.CharField(max_length=30)
    #bookname=models.CharField(max_length=50)
    #book_author=models.CharField(max_length=50)
    #publish_date=models.DateField(max_length=50,default="2022-02-24")
    issuedate=models.DateField(max_length=20,null=True)
    returndate=models.DateField(max_length=20,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    #book=models.ManyToManyField(books)
    #book=models.ForeignKey(books)
    book=models.ForeignKey(books,on_delete=models.CASCADE,null=True)

    #def get_books(self):
    #    return ", ".join([str(i) for i in self.book.all()]) # str(i) will display the names else page will give error

    class Meta:
        db_table='bookissue'


    def __str__(self):
        return str(self.book)

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'DB_NAME',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',  
        'PORT': '3306',
    }
}
'''