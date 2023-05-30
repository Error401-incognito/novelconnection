from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.db.models.signals import post_save
from django.utils.html import mark_safe

from userauths.models import User, Profile, user_directory_path

from PIL import Image
from shortuuid.django_fields import ShortUUIDField



VISIBILITY = (
    ("only_me","Only Me"),
    ("everyone","Everyone"),
)

FRIEND_REQUEST = (
    ("pending","pending"),
    ("accept","Accept"),
    ("reject","Reject"),
)


NOTIFICATION_TYPE = (
    ("Friend Request", "Friend Request"),
    ("New Follower", "New Follower"),
    ("New Like", "New Like"),
    ("New Comment", "New Comment"),
    

)


class FriendRequest(models.Model):
    fid = ShortUUIDField(length=7, max_length=25, alphabet="abcdefghijklmnopqrstuvxyz123")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reciever")
    status = models.CharField(max_length=10, default="pending", choices=FRIEND_REQUEST)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}"
    
    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "Friend Request"

class Friend(models.Model):
    fid = ShortUUIDField(length=7, max_length=25, alphabet="abcdefghijklmnopqrstuvxyz123")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friend")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"
    
    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "Friend"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=500, blank=True ,null=True)
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    video = models.FileField(upload_to=user_directory_path, null=True, blank=True)
    visibility = models.CharField(max_length=10, default="everyone", choices=VISIBILITY)
    date = models.DateTimeField(auto_now_add=True)
    pid = ShortUUIDField(length=7, max_length=25, alphabet="abcdefghijklmnopqrstuvxyz123")
    likes = models.ManyToManyField(User, blank=True, related_name="likes")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "Post"

    def thumbnail(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" object-fit:"cover" style="border-radius: 30px;" />' % (self.image))

    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, blank=True ,null=True)
    date = models.DateTimeField(auto_now_add=True)
    cid = ShortUUIDField(length=7, max_length=25, alphabet="abcdefghijklmnopqrstuvxyz123")
    likes = models.ManyToManyField(User, blank=True, related_name="comment_likes")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "Comment"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    notification_type = models.CharField(max_length=100, choices=NOTIFICATION_TYPE, default="none")
    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    nid = ShortUUIDField(length=10, max_length=25, alphabet="abcdefghijklmnopqrstuvxyz")
    
    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "Notification"

    def __str__(self):
        return f"{self.user} - {self.notification_type}"
