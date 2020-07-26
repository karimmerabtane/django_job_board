from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# admin.site.register(Post)


class PostAd(SummernoteModelAdmin):
    summernote_fields = ('body',)


class CommentAd(SummernoteModelAdmin):
    summernote_fields = ('body',)
admin.site.register(Post,PostAd)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['title', 'slug', 'author', 'publish', 'status']
#     list_filter = ['status', 'created', 'publish', 'author']
#     search_fields = ['title', 'body']
#     prepopulated_fields = {'slug': ('title',)}
#     row_id_fields = ['author', ]
#     date_hierarchy = 'publish'
#     ordering = ['status', 'publish']


admin.site.register(Comment,CommentAd)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'post', 'created', 'active']
#     list_filter = ['active', 'created', 'updated']
#     search_fields = ['name', 'email', 'body']
