from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import HomePage, Slide, IconBlurb, Portfolio

# Register your models here.
class SlideAdminInline(TabularDynamicInlineAdmin):
    model = Slide

class IconAdminInline(TabularDynamicInlineAdmin):
    model = IconBlurb

class HomePageAdmin(PageAdmin):
    model = HomePage
    inlines = [
        SlideAdminInline,
        IconAdminInline,
    ]

admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Portfolio, PageAdmin)
