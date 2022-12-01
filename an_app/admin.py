from django.contrib import admin
from an_app.models import PostModel


@admin.register(PostModel)
class PostsAdmin(admin.ModelAdmin):
    pass
