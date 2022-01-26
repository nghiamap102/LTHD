from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):
    class Meta:
        unique_together = ['phone', 'username']

    address = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=12, null=True,blank=True)
    avatar = models.ImageField(upload_to='static/user/%Y/%m', null=True)
    avatar_url = models.CharField( max_length=1000,null=True,blank=True)
    birthdate = models.DateField(null=True)
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.last_name + " " + self.first_name


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    activeStaff = models.BooleanField(default=False)


class ItemBase(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=50, null=False)
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


class TagTourDetail(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class TagCountry(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class TagBlog(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Departure(ItemBase):
    class Meta:
        ordering = ["id"]
        unique_together = ('name', 'active')
    image = models.ImageField(upload_to='static/tour/%Y/%m')
    content = models.TextField(null=True, blank=True)
    tag = models.ManyToManyField('TagCountry', related_name="departure", blank=True, null=True)

    def __str__(self):
        return self.name

    # def get_tags(self):
    #     return "\n".join([p.name for p in self.tags.all()])


class Destination(ItemBase):
    class Meta:
        ordering = ['id']
        unique_together = ('name', 'active')
    image = models.ImageField(upload_to='static/destination/%Y/%m')
    content = models.TextField(null=True, blank=True)
    tag = models.ManyToManyField('TagCountry', related_name="tour", blank=True, null=True)

    def __str__(self):
        return self.name


class TourDetail(ItemBase):
    class Meta:
        unique_together = ('name', 'departure')
        ordering = ["created_date"]

    image = models.ImageField(upload_to='static/tour_detail/%Y/%m')

    slot = models.IntegerField(default=40)  ## Còn bn chỗ
    time_start = models.DateTimeField(null=True)  # time bắt đầu
    duration = models.IntegerField()  # so ngay cua tour

    content = RichTextField(null=True)
    departure = models.ForeignKey(Departure, related_name="detail", on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, related_name="detail", on_delete=models.CASCADE)
    transport = models.ManyToManyField('Transport', related_name='detail', blank=True, null=True)

    price_room = models.IntegerField(null=True)
    price_tour = models.IntegerField(null=True)
    discount = models.IntegerField(null=True, default=0)

    total = models.IntegerField(null=True)

    tag = models.ManyToManyField('TagTourDetail', related_name="detail", blank=True, null=True)
    img_detail = models.ManyToManyField('ImgDetail', related_name="detail", blank=True, null=True)

    def __str__(self):
        return self.name


class ImgDetail(models.Model):
    # name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='static/img_detail/%Y/%m')

    def __str__(self):
        return 'http://127.0.0.1:8000/' + self.image.name


class Blog(models.Model):
    name = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to='static/blog/%Y/%m')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    content = RichTextUploadingField(null=True)
    decription = models.TextField(null=True)
    tag = models.ManyToManyField('TagBlog', related_name="blog", blank=True, null=True)
    img_detail = models.ManyToManyField('ImgDetail', related_name="blog", blank=True, null=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    class Meta:
        unique_together = ['tour_detail', 'customer', 'status']

    BOOKING_STATUS = (
        ('p', 'Booking processing'),
        ('a', 'Booking accepted'),
        ('c', 'Booking canceled')
    )

    tour_detail = models.ForeignKey(TourDetail, related_name="booking", on_delete=models.CASCADE, null=False)
    customer = models.ForeignKey(User, related_name="booking", on_delete=models.CASCADE, null=True)

    adult = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    children = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    status = models.CharField(max_length=1, choices=BOOKING_STATUS, default="p")
    room = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    total = models.IntegerField(null=True)
    point_used = models.IntegerField(null=True)

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
    rate = models.PositiveSmallIntegerField(default=1)

    class Meta:
        unique_together = ["tour", "creator"]


class Like(models.Model):
    class Meta:
        unique_together = ["blog", "creator"]

    LIKE, HEART, HAHA, SAD, ANGRY = range(5)
    ACTIONS = [
        (LIKE, 'like'),
        (HEART, 'heart'),
        (HAHA, 'haha'),
        (SAD, 'sad'),
        (ANGRY, 'angry'),
    ]
    type = models.PositiveSmallIntegerField(choices=ACTIONS, default=LIKE)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog, related_name="like", on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class Views(models.Model):
    created_date = models.DateTimeField(null=True)
    update_date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)


class Hotel(ItemBase):
    image = models.ImageField(upload_to='static/hotel/%Y/%m')
    tour_detail = models.OneToOneField(TourDetail,
                                       on_delete=models.CASCADE,
                                       primary_key=True)
    address = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=12, null=False)
    email = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

# class LikeList(models.Model):
#     user = models.ForeignKey(User ,related_name="likelist" , on_delete=models.CASCADE)
