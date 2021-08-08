from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')


# class Staff(AbstractUser):
#     avatar =models.ImageField( upload_to= 'uploads/%Y/%m')

class ItemBase(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=50, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        self.name


class Hotel(ItemBase):
    imageHotel = models.ImageField(upload_to='hotel/%Y/%m')
    address = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=12, null=False)
    email = models.CharField(max_length=50, null=False)
    price = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.name

class Transport(ItemBase):

    price = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.name

class ToursTotal(ItemBase):
    imageTours = models.ImageField(upload_to='tours/%Y/%m')
    count = models.CharField(max_length=20, null=True)
    tags = models.ManyToManyField('Tag', related_name="tours", blank=True, null=True)

    def __str__(self):
        return self.name

    def get_tags(self):
        return "\n".join([p.name for p in self.tags.all()])


class ToursDetail(ItemBase):
    class Meta:
        unique_together = ('tourid', 'tours')

    tourid = models.CharField(max_length=20, null=False)
    price = models.CharField(max_length=100, null=False)
    vat = models.CharField(max_length=100, null=False)
    timestart = models.DateTimeField()
    timefinish = models.DateTimeField()
    content = RichTextField()
    tours = models.ForeignKey(ToursTotal, on_delete=models.CASCADE, null=False)
    hotel = models.ManyToManyField('Hotel', related_name="toursdetail", blank=True, null=True)
    transport = models.ManyToManyField('Transport', related_name="toursdetail", blank=True, null=True)
    def __str__(self):
        return self.tourid

    def get_hotels(self):
        return "\n".join([p.name for p in self.hotel.all()])

    def get_transport(self):
        return "\n".join([p.name for p in self.transport.all()])


class Tag(ItemBase):

    decription = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

# class Bill (User):
#     tours = models.ForeignKey(ToursTotal, on_delete=models.CASCADE, null=False)
#     hotel = models.ManyToManyField('Hotel', related_name="toursdetail", blank=True, null=True)




# class Feedback :
#     thông tin khách hàng kế thừa itembase ở đây
#     cmt = models.TextField()
#     rate = models.TextField()
#
#

# class Employee(models.Model):
#
#
# class Static ():
#     countTour =
#     income =
#     quy =
#     year
#
# class News (models.Model):
#     content = RichTextField()
