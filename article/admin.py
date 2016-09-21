from django.contrib import admin

# Register your models here.
from article.models import Article
from django.db import models

from pagedown.widgets import AdminPagedownWidget

# Register your models here.

class FooModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }
admin.site.register(Article, FooModelAdmin)

