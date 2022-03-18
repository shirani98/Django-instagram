from django.contrib import admin

from post.models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("body",)}
    list_display = ('user', 'slug', 'created', 'body')
    list_filter = ('created',)
    search_fields = ('body','user__username')
    list_display_links = ('user', 'slug')
    fieldsets = (
        ('Main', {'fields': ('user', 'image', 'body', 'slug')}),
    )


admin.site.register(Post, PostAdmin)
