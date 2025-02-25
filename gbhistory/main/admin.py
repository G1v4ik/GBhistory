from django.contrib import admin

from .models import Blog, BlogCollect, BlogContent


class BlogContentInline(admin.TabularInline):
    model = BlogContent



@admin.register(BlogCollect)
class BlogColletAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'previewTitle', )
    list_display_links = ('id', 'previewTitle', )
    prepopulated_fields = {'slug': ('previewTitle', )}
    inlines = [BlogContentInline,]

