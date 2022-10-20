from django.contrib import admin
from webapp.models import Post


# class PostAdmin(admin.ModelAdmin):
#     fields = ['title', 'body']


admin.site.register(Post)
