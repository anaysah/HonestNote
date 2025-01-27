from django.contrib import admin
from .models import Post, Category, Profile, Comment,FeaturedBlog

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(FeaturedBlog)


from .models import WebsiteSettings

@admin.register(WebsiteSettings)
class WebsiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('website_name', 'about_text')
    fieldsets = (
        (None, {
            'fields': ('website_name', 'about_text')
        }),
        ('Social Media Links', {
            'fields': ('social_media_links',),
            'description': 'Enter social media links as a JSON object. Example: {"facebook": "https://facebook.com", "twitter": "https://twitter.com"}'
        }),
    )