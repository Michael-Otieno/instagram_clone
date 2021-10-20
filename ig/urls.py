from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('', views.home,name="home"),
    url('user/<str:username>', views.user_profile,name="user_profile"),
    url('add_comment', views.add_comment,name="add_comment"),
    url('like/<int:postid>',views.like_post,name='like_post'),
    url('create/post', views.add_post, name='add_post'),
    url('edit/<str:username>', views.edit_profile, name='edit_profile'),
]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    