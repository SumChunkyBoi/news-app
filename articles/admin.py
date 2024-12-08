# articles/admin.py
from django.contrib import admin
from .models import Article, Comment

class CommentInline(admin.TabularInline):  # new
    model = Comment  # Inline to display comments on the Article admin page

class ArticleAdmin(admin.ModelAdmin):  # new
    inlines = [  # Display comments as inline on the article edit page
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
