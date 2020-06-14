from django.urls import path
from blog import views
from blog.views import AboutView, PostListView, PostDetailView, CreatePostView, PostDeleteView, UpdatePostView, \
    DraftPostView

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', UpdatePostView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove/', PostDeleteView.as_view(), name='post_remove'),
    path('draft/', DraftPostView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/comment',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve',views.approve_comment,name='approve_comment'),
    path('comment/<int:pk>/delete', views.remove_comment, name='remove_comment'),
    path('post/<int:pk>/publish',views.publish_post,name='publish_post'),
]
