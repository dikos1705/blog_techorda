from .views import PostList,PostDetail,PostUpdate,PostDelete,PostCreate
from django.urls import path

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('new-post', PostCreate.as_view(), name='create_post'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    # path('<slug:slug>/', post_detail, name='post-detail'),
    path('<slug:slug>/update', PostUpdate.as_view(), name='post_update'),
    path('<slug:slug>/delete', PostDelete.as_view(), name='post_delete'),
]