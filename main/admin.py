from django.contrib import admin
from .models import Post, Reaction, Profile, Comment, Follow

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Follow)
admin.site.register(Comment)
admin.site.register(Reaction)
