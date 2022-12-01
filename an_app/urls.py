from django.contrib import admin
from django.urls import path
from an_app.views import DemoView, MakeException

urlpatterns = [
    path('posts/create/', DemoView.as_view(), name='post_create',
         kwargs={'create': True}),
    path('posts/<int:post_id>/', DemoView.as_view(), name='post_view'),
    path('posts/', DemoView.as_view(), name='post_index'),
    path('except/', MakeException.as_view(), name='except'),
]
