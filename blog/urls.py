from django.urls import path, include
from .api import BlogAPI, BlogContentViewAPI, BlogContentViewAllAPI, BlogCategoryAPI, BlogDetailAPI, GetBlogCommentViewAPI, BlogCommentAPI
urlpatterns = [
    path('api/blog', BlogAPI.as_view()),
    path('api/blog/all', BlogContentViewAllAPI.as_view()),
    path('api/blog/get', BlogContentViewAPI.as_view()),
    path('api/blog/<int:pk>', BlogDetailAPI.as_view()),
    path('api/blog/category', BlogCategoryAPI.as_view()),
    path('api/blog/comment', BlogCommentAPI.as_view()),
    path('api/blog/comment/all/<int:pk>', GetBlogCommentViewAPI.as_view())
]
