from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):
    address = models.CharField(max_length=50, null=True)
    phone = models.IntegerField(null=True)
    avatar = models.ImageField(upload_to='static/user/%Y/%m')
    birthdate = models.DateTimeField(null=True)

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
        return self.name


class TourTotal(ItemBase):
    class Meta:
        ordering = ["id"]

    content = models.TextField(null=False, blank=True)
    tags = models.ManyToManyField('Tag', related_name="tours", blank=True, null=True)

    def __str__(self):
        return self.name
    #
    # def get_tags(self):
    #     return "\n".join([p.name for p in self.tags.all()])


class Transport(models.Model):
    name = models.CharField(max_length=50, null=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Hotel(ItemBase):
    address = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=12, null=False)
    email = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class TourDetail(ItemBase):
    class Meta:
        unique_together = ('name', 'tour')

    price = models.IntegerField()  # gia tour
    discount = models.IntegerField(default=0)
    status = models.IntegerField(default=40)  ## Còn bn chỗ

    time_start = models.DateTimeField()  # time bắt đầu
    duration = models.IntegerField()  # so ngay cua tour

    content = RichTextField()
    tour = models.ForeignKey(TourTotal, related_name="detail", on_delete=models.CASCADE)
    transport = models.ManyToManyField(Transport, related_name='detail', blank=True, null=True)
    hotel = models.ForeignKey(Hotel, related_name='detail', on_delete=models.SET_NULL, null=True)

    image_detail = models.ManyToManyField('ImgDetail', related_name="detail", blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def get_hotels(self):
        return "\n".join([p.name for p in self.hotel.all()])


class Blog(ItemBase):
    content = RichTextUploadingField()
    tags = models.ManyToManyField(Tag, related_name='blog', blank=True, null=True)
    tour_detail = models.ForeignKey(TourDetail, related_name='blog', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class ImgDetail(models.Model):
    image = models.ImageField(upload_to='static/detail/%Y/%m')
    tour_detail = models.ForeignKey(TourDetail, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return 'http://127.0.0.1:8000/' + self.image.name


class ActionBase(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    tour = models.ForeignKey(TourDetail, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        unique_together = ["tour", "creator"]


class Rating(ActionBase):
    rate = models.PositiveSmallIntegerField(default=0)


class TourDetailViews(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    tour_detail = models.OneToOneField(TourDetail, on_delete=models.CASCADE)


class Booking(models.Model):
    class Meta:
        unique_together = ['tour_detail', 'customer']

    BOOKING_STATUS = (
        ('Booking processing', 'Booking processing'),
        ('Booking accepted', 'Booking accepted'),
        ('Booking canceled', 'Booking canceled')
    )

    tour_detail = models.ForeignKey(TourDetail, related_name="booking", on_delete=models.CASCADE, null=False)
    customer = models.ForeignKey(User, related_name="booking", on_delete=models.CASCADE, null=True)

    content = models.TextField(null=True)
    adult = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    children = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    status = models.CharField(max_length=25, choices=BOOKING_STATUS, default="Booking processing")

    room = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    room_price = models.IntegerField(null=True)

    created_date = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def total(self):
        return (self.tour_detail.final_price * self.adult
                + int(self.tour_detail.final_price * self.children) * 50 / 100
                + (self.room * self.room_price))


class Room_price(models.Model):
    tour_detail = models.ForeignKey(TourDetail, related_name="room_price", on_delete=models.SET_NULL, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.tour_detail


class Point(models.Model):
    customer = models.ForeignKey(User, related_name="point", on_delete=models.CASCADE, null=True)
    point = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.customer


class Comment(models.Model):
    class Meta:
        ordering = ["-id"]

    content = models.TextField()
    tour_detail = models.ForeignKey(TourDetail, related_name="comment", on_delete=models.CASCADE, null=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

# class Action(ActionBase):
#     LIKE, HAHA, HEART = range(3)
#     ACTIONS = [
#         (LIKE, 'like'),
#         (HAHA, 'haha'),
#         (HEART, 'heart')
#     ]
#     type = models.PositiveSmallIntegerField(choices=ACTIONS, default=LIKE)
#
