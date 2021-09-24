from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):
    avatar = models.ImageField(upload_to='static/uploads/%Y/%m')

    def __str__(self):
        return self.last_name + " " + self.first_name


# class Staff(AbstractUser):
#     avatar =models.ImageField( upload_to= 'uploads/%Y/%m')

class ItemBase(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to='static/%Y/%m')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        self.name


class Hotel(ItemBase):
    address = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=12, null=False)
    email = models.CharField(max_length=50, null=False)
    price = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Transport(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.CharField(max_length=50, null=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ToursTotal(ItemBase):
    class Meta:
        ordering = ["-id"]

    decription = models.TextField(null=False, blank=True)
    tags = models.ManyToManyField('Tag', related_name="tours", blank=True, null=True)

    def __str__(self):
        return self.name
    #
    # def get_tags(self):
    #     return "\n".join([p.name for p in self.tags.all()])


class ToursDetail(ItemBase):
    class Meta:
        unique_together = ('name', 'tours')

    price = models.CharField(max_length=100, null=False)
    vat = models.CharField(max_length=100, null=False)
    timestart = models.DateTimeField()
    timefinish = models.DateTimeField()
    decription = models.TextField(null=False, blank=True)
    tours = models.ForeignKey(ToursTotal, related_name="details", on_delete=models.CASCADE)
    hotel = models.ManyToManyField('Hotel', related_name="details", blank=True, null=True)
    transport = models.ManyToManyField('Transport', related_name="details", blank=True, null=True)
    cmt = models.ManyToManyField('Comment', related_name="details", blank=True, null=True)
    imagedetail = models.ManyToManyField('ImgDetail', related_name="details", blank=True, null=True)

    def __str__(self):
        return self.name

    # def get_hotels(self):
    #     return "\n".join([p.name for p in self.hotel.all()])
    #
    # def get_transport(self):
    #     return "\n".join([p.name for p in self.transport.all()])
    #
    # def get_cmt(self):
    #     return "\n".join([p.name for p in self.cmt.all()])


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)


    def __str__(self):
        return self.name


class Comment(models.Model):
    cmt = models.TextField()
    tourdetail = models.ForeignKey(ToursDetail, on_delete=models.CASCADE, null=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class ImgDetail(models.Model):
    image = models.ImageField(upload_to='static/detail/%Y/%m')
    tourdetail = models.ForeignKey(ToursDetail, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.image.name


class ActionBase(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    tour = models.ForeignKey(ToursDetail, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Action(ActionBase):
    LIKE, HAHA, HEART = range(3)
    ACTIONS = [
        (LIKE, 'like'),
        (HAHA, 'haha'),
        (HEART, 'heart')
    ]
    type = models.PositiveSmallIntegerField(choices=ACTIONS, default=LIKE)


class Rating(ActionBase):
    rate = models.PositiveSmallIntegerField(default=0)


class TourDetailViews(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    tourdetail = models.OneToOneField(ToursDetail, on_delete=models.CASCADE)

# class Bill (ItemBase):
#     tours = models.ForeignKey(ToursTotal, on_delete=models.CASCADE, null=False)
#     hotel = models.ForeignKey('Hotel',on_delete=models.SET_NULL,null=True)
#     transport = models.ForeignKey('Transport',on_delete=models.SET_NULL,null=True)
#     total = models.CharField(max_length=2 ,null=False)
#     def __str__(self):
#         return self.total

# class Employee(models.Model):
#
#
# class Static ():
#     countTour =
#     income =
#     quy =
#     year
#
# class News (ItemBase):
#     imageNews = models.ImageField(upload_to= 'news/%Y/%m')
#     content = RichTextField()
#
#     def __str__(self):
#         return self.name
