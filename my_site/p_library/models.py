from django.db import models
import uuid
from p_library.validators import validate_zero



# Create your models here.

class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)
    
    def __str__(self):
        return self.full_name

class Redaction(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False, verbose_name="UUID")
    name = models.TextField()

    def __str__(self):
        return self.name

class Friend(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


	
class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField(default=2)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    redact = models.ForeignKey(Redaction,on_delete=models.SET_NULL, related_name='books', blank=True, null=True)
    friends = models.ManyToManyField(Friend, blank=True, through='Rent', related_name='friendrent')

    def __str__(self):
        return self.title

class Rent(models.Model):
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.SmallIntegerField()

    def save(self, *args, **kwargs):
        from django.http import HttpResponseServerError
        from p_library.models import Book
        book = Book.objects.get(id=self.book.id)
        book.copy_count -= self.count
        book.save()
        super(Rent, self).save(*args, **kwargs)



