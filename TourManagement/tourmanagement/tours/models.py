from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):
    address = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=12, null=True)
    avatar = models.ImageField(upload_to='static/user/%Y/%m', null=True)
    birthdate = models.DateField(null=True)
    active_staff = models.BooleanField(default=False)
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.last_name + " " + self.first_name


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


class Transport(models.Model):
    name = models.CharField(max_length=50, null=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class TourTotal(ItemBase):
    class Meta:
        ordering = ["id"]
        unique_together = ('name', 'active')

    content = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name="tours", blank=True, null=True)

    def __str__(self):
        return self.name

    # def get_tags(self):
    #     return "\n".join([p.name for p in self.tags.all()])


class TourDetail(ItemBase):
    class Meta:
        unique_together = ('name', 'tour')
        ordering = ["created_date"]

    slot = models.IntegerField(default=40)  ## Còn bn chỗ

    time_start = models.DateTimeField(null=True)  # time bắt đầu
    duration = models.IntegerField()  # so ngay cua tour

    content = RichTextField(null=True)
    tour = models.ForeignKey(TourTotal, related_name="detail", on_delete=models.CASCADE)
    transport = models.ManyToManyField('Transport', related_name='detail', blank=True, null=True)

    price_room = models.IntegerField(null=True)

    price_tour = models.IntegerField(null=True)
    discount = models.IntegerField(null=True,default=0)

    total = models.IntegerField(null=True)

    # hotel = models.ForeignKey(Hotel, related_name='detail', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to='static/blog/%Y/%m')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    content = RichTextUploadingField()
    tour_detail = models.ForeignKey(TourDetail, related_name='blog', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class ImgDetail(models.Model):
    class Meta:
        unique_together = ['image', 'tour_detail']

    image = models.ImageField(upload_to='static/detail/%Y/%m')
    tour_detail = models.ForeignKey(TourDetail, related_name="img_detail", on_delete=models.CASCADE, null=False)

    def __str__(self):
        return 'http://127.0.0.1:8000/' + self.image.name


class Booking(models.Model):
    class Meta:
        unique_together = ['tour_detail', 'customer']

    BOOKING_STATUS = (
        ('p', 'Booking processing'),
        ('a', 'Booking accepted'),
        ('c', 'Booking canceled')
    )

    tour_detail = models.ForeignKey(TourDetail, related_name="booking", on_delete=models.CASCADE, null=False)
    customer = models.ForeignKey(User, related_name="booking", on_delete=models.CASCADE, null=True)

    content = models.TextField(null=True)
    adult = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    children = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    status = models.CharField(max_length=1, choices=BOOKING_STATUS, default="p")

    room = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    created_date = models.DateTimeField(auto_now_add=True, null=True)

    total = models.IntegerField(null=True)

    def __int__(self):
        return self.total


class CommentTourDetail(models.Model):
    class Meta:
        ordering = ["-id"]

    content = models.TextField()
    tour_detail = models.ForeignKey(TourDetail, related_name="cmt_tour", on_delete=models.CASCADE, null=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class CommentBlog(models.Model):
    class Meta:
        ordering = ["-id"]

    content = models.TextField()
    blog = models.ForeignKey(Blog, related_name="cmt_blog", on_delete=models.CASCADE, null=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class Rating(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    tour = models.ForeignKey(TourDetail, related_name="rating", on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(default=0)

    class Meta:
        unique_together = ["tour", "creator"]


class Like(models.Model):
    class Meta:
        unique_together = ["blog", "creator"]

    LIKE, HAHA, HEART, SAD, ANGRY = range(5)
    ACTIONS = [
        (LIKE, 'like'),
        (HAHA, 'haha'),
        (HEART, 'heart'),
        (SAD, 'sad'),
        (ANGRY, 'angry'),
    ]
    type = models.PositiveSmallIntegerField(choices=ACTIONS, default=LIKE)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog, related_name="like", on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class TourDetailViews(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    tour_detail = models.OneToOneField(TourDetail, on_delete=models.CASCADE)


class Hotel(ItemBase):
    tour_detail = models.OneToOneField(TourDetail,
                                       on_delete=models.CASCADE,
                                       primary_key=True)
    address = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=12, null=False)
    email = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name
