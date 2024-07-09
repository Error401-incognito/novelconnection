from django.urls import path 
from core import views 
from core.views import pages_view,albums_view,chats_friend_view

app_name = "core"

urlpatterns = [
    path("", views.index, name="feed"),
    path("post/<slug:slug>/", views.post_detail, name="post-detail"),

    # Chat Feature
    path("core/inbox/", views.inbox, name="inbox"),
    path("core/inbox/<username>/", views.inbox_detail, name="inbox_detail"),

    # Group CHat
    path("core/group-inbox/", views.group_inbox, name="group_inbox"),
    path("core/group-inbox/<slug:slug>/", views.group_inbox_detail, name="group_inbox_detail"),
    path("core/create-group/", views.create_group_page, name="create_group_page"),
    path('groups.html', views.groups_view, name='groups'),
    path('pages.html', pages_view, name='pages'),
    path('albums.html', albums_view, name='albums'),
    path('timeline-page.html', views.timeline_page, name='timeline_page'),
    path('videos.html', views.videos_page, name='videos_page'),

    # Join & leave Group
    path("core/join-group-page/<slug:slug>/", views.join_group_chat_page, name="join_group_chat_page"),
    path("core/join-group/<slug:slug>/", views.join_group_chat, name="join_group"),
    path("core/leave-group/<slug:slug>/", views.leave_group_chat, name="leave_group_chat"),
    path('chats-friend.html', chats_friend_view, name='chats_friend'), 
    # Games
    path("core/all-games/", views.games, name="games"),
    path("core/stack_brick/", views.stack_brick, name="stack_brick"),

    # Search
    path('search/', views.search_users, name='search_users'),

    # Load more post
    path('load_more_posts/', views.load_more_posts, name='load_more_posts'),




    # Ajax URLs
    path("create-post/", views.create_post, name="create-post"),
    path("like-post/", views.like_post, name="like-post"),
    path("comment-post/", views.comment_on_post, name="comment-post"),
    path("like-comment/", views.like_comment, name="like-comment"),
    path("reply-comment/", views.reply_comment, name="reply-comment"),
    path("delete-comment/", views.delete_comment, name="delete-comment"),
    path("add-friend/", views.add_friend, name="add-friend"),
    path("accept-friend-request/", views.accept_friend_request, name="accept-friend-request"),
    path("reject-friend-request/", views.reject_friend_request, name="reject-friend-request"),
    path("unfriend/", views.unfriend, name="unfriend"),
    path("block-user/", views.block_user, name="block_user"),
]