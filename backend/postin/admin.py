from django.contrib import admin
from .models import Post, User

class AdminUser(admin.ModelAdmin):
    list_display = ["id", "nickname"]

class AdminPost(admin.ModelAdmin):
    list_display = ["id", "tittle"]


# Register your models here.
admin.site.register(Post, AdminPost)
admin.site.register(User, AdminUser) 