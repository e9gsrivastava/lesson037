from django.db import models
import random
import datetime
from django.utils import timezone
# Create your models here.

class Profile(models.Model):
    slug = models.SlugField()
    username = models.CharField(unique=True, max_length=60)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.IntegerField(unique=True)
    address = models.TextField()

    def random_data(self):
        random_names = ['Tom', 'Nick', 'John', 'Yoda', 'Shivansh', 'Akash', 'Akbar']
        streets=['Baner','CP','Ifco chowk']
        cities=['NYC','Delhi','Pune','Mumbai']
        my_list = []
        for i in range(50000):
            usernames = f'{random.choice(random_names)}{i}'
            slugs = f'{usernames}{i}'
            emails = f'{usernames}{i}@lib.com'
            phones= random.randint(1000000000, 9999999999)
            addresss = f'{random.randint(1, 1000)} {random.choice(streets)} Street, {random.choice(cities)} City '
            obj = Profile(slug=slugs, username=usernames,email=emails,phone=phones,address=addresss)

            my_list.append(obj)

        Profile.objects.bulk_create(my_list)


class Author(models.Model):
    slug=models.SlugField()
    name=models.CharField(max_length=60,unique=True)
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE)
    
    def author_random_data(self):
        my_list=[]
        p = list(Profile.objects.all())
        random_names = ['Tom', 'Nick', 'John', 'Yoda', 'Shivansh', 'Akash', 'Akbar']
        for i in range(50000):
            names = f'{random.choice(random_names)}{i}'
            slugs = f'{names}{i}'
            obj = Author(slug=slugs, name=names,profile=p[i])

            my_list.append(obj)

        Author.objects.bulk_create(my_list)

    def author_list(self):
        p =Profile.objects.all()
        # use related name
        answer=[i.name for i in p]
        return answer

class Publisher(models.Model):
    slug=models.SlugField()
    name=models.CharField(max_length=50)
    website=models.URLField()
    email=models.EmailField()
    address=models.TextField()

    def publisher_random_data(self):
        random_names = ['Shivansh', 'Akbar', 'Kunal', 'Reacher']
        website_names=['TMC','Ncert','Rd Sharma']
        cities=['NYC','Delhi','Pune','Mumbai']
        streets=['Baner','CP','Ifco chowk']
        my_list = []
        for i in range(50000):
            names = f'{random.choice(random_names)}{i}'
            slugs = f'{names}{i}'
            websites= f'{random.choice(website_names)}{i}@book.com'
            emails = f'{names}{i}@lib.com'
            
            addresss = f'{random.randint(1, 1000)} {random.choice(streets)} Street, {random.choice(cities)} City '
            obj = Publisher(slug=slugs, name=names,email=emails,website=websites,address=addresss)
            my_list.append(obj)

        Publisher.objects.bulk_create(my_list)


class Book(models.Model):
    slug=models.SlugField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    date_of_pub=models.DateField()

    def publisher_random_data(self):
        random_titles = ['Alchemy', 'Nature', 'Gandhi', 'PM']
        auth=list(Author.objects.all())
        p = list(Publisher.objects.all())
        my_list = []
        for i in range(50000):
            titles = f'{random.choice(random_titles)}{i}'
            slugs = f'{titles}{i}'
            date_of_pubs = timezone.now() - timezone.timedelta(days=random.randint(1, 36500))
            
            obj = Book(slug=slugs, title=titles ,date_of_pub=date_of_pubs,author=auth[i],publisher=p[i])
            my_list.append(obj)

        Book.objects.bulk_create(my_list)





class Collection(models.Model):
    slug=models.SlugField()
    name=models.CharField(max_length=30)
    book=models.ManyToManyField(Book)

    def collections_random_data(self):
        random_names = ['Shivansh', 'Akbar', 'Kunal', 'Reacher']
        my_list = []

        for i in range(50000):
            names = f'{random.choice(random_names)}{i}'
            slugs = f'{names}{i}'
            
            obj = Collection(slug=slugs, name=names)
            obj.save()
            obj.book.add(random.choice(Book.objects.all()))
            # my_list.append(obj)

        # Collection.objects.bulk_create(my_list)




