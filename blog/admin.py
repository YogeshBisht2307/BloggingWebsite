from django.contrib import admin
from blog.models import Author, BlogSubCategory,BlogCategory, Blog, Tag, Comment,Contact,Web_detail,SEO_Configuration

class TagConfiguration(admin.TabularInline):
    model = Tag

class BlogConfiguration(admin.ModelAdmin):
    inlines = [TagConfiguration]
    class Media:
        css = {
            "all":("blog/css/style.css",)
        }
        js = ('blog/js/main.js',)

class Web_detail_Configuration(admin.ModelAdmin):
    model = Web_detail
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

class SEO_Configuration_admin(admin.ModelAdmin):
    model = SEO_Configuration
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Author)
admin.site.register(BlogCategory)
admin.site.register(BlogSubCategory)
admin.site.register(Blog , BlogConfiguration)
admin.site.register(Comment)
admin.site.register(Web_detail,Web_detail_Configuration)
admin.site.register(SEO_Configuration,SEO_Configuration_admin)