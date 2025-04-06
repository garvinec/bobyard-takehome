from django.urls import path, include
from .views import CommentViewSet, get_comments, create_comment, update_comment, delete_comment
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('comments/', include('rest_framework.urls')),
    path('comments/get', get_comments, name='get_comments'),
    path('comments/create', create_comment, name='create_comment'),
    path('comments/update/<str:pk>', update_comment, name='update_comment'),
    path('comments/delete/<str:pk>', delete_comment, name='delete_comment'),
]
