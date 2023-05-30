from django.contrib import admin
from core.models import Post, Friend, FriendRequest, Notification, Comment


class FriendRequestAdmin(admin.ModelAdmin):
    list_editable = ['status']
    list_display = ['sender', 'reciever', 'status']

class FriendAdmin(admin.ModelAdmin):
    list_display = ['user', 'friend']

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'notification_type', 'is_read']


class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'visibility']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'comment', 'active']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'comment', 'active']


admin.site.register(Notification, NotificationAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(FriendRequest, FriendRequestAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)