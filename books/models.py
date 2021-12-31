from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 50)
    num_of_pages = models.IntegerField(verbose_name='Page number',help_text='enter man')
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="my_books")

    class Meta:
       ordering = ['-num_of_pages'] 

    def __str__(self):
        return f'{self.title}-{self.author}'
    