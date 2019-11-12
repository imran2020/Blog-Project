from django.contrib import admin
from .models import *

# Register your models here.

class authorModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__","details"]
    class Meta:
        model=author

class articleModel(admin.ModelAdmin):
    list_display = ["__str__","posted_on"]
    search_fields = ["__str__","title"]
    list_filter = ["title","category"]
    class Meta:
        model=article

class categoryModel(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    class Meta:
        model=category
admin.site.register(author,authorModel)
admin.site.register(category,categoryModel)
admin.site.register(article,articleModel)
admin.site.register(comment)
admin.site.register(post)
admin.site.register(post_comment)