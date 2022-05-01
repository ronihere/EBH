from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name= models.CharField('Categories', max_length=50)
    slug = models.SlugField(max_length=100)
    def __str__(self):
        return self.name
class Book(models.Model):
    title= models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    cover_image=models.ImageField(upload_to='img',blank=True,null=True)
    author=models.CharField(max_length=100)
    summary=models.TextField(max_length=240)
    category=models.ManyToManyField(Category,related_name='books')
    pdf = models.FileField(upload_to='pdf')
    recommended_books=models.BooleanField(default=False)
    fiction_books= models.BooleanField(default=False)
    business_books= models.BooleanField(default=False)
    def __str__(self):
        return self.title
RATE_CHOICES= [
    (1,'1 = Trash'),
    (2,'2 = Bad'),
    (3,'3 = Good'),
    (4,'4 = Very good'),
    (5,'5 = Perfect'),
]

class Review(models.Model):
    bookm=models.ForeignKey(Book,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=400)
    rating = models.SmallIntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return self.bookm.title
