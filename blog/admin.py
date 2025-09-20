from django.contrib import admin
from blog.models import Post, Tag, Comment


admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)

class PostAdmin(admin.ModelAdmin):
    search_fields=['title',]

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'text']
    raw_id_fields = ('post', 'author')
    search_fields = ['author__username', 'post__title', 'text']