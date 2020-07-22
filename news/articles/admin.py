from django.contrib import admin

from articles.models import Article, Comment

class CommentInline(admin.TabularInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
