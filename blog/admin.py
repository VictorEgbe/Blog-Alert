from django.contrib import admin

from .models import BlogPost, Comment


class BlogPostModelAdmin(admin.ModelAdmin):

    list_display = ['title', 'author', 'created', 'updated']
    search_fields = ['title', 'content', 'author__username']
    list_filter = ['created']

    class Meta:
        model = BlogPost


admin.site.register(BlogPost, BlogPostModelAdmin)


class CommentModelAdmin(admin.ModelAdmin):
    list_filter = ['created']
    search_fields = ['comment', 'author__username']

    class Meta:
        model = Comment


admin.site.register(Comment, CommentModelAdmin)
