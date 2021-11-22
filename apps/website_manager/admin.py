from django.contrib import admin
from .models import PortfolioItem
from django.utils.html import format_html


@admin.register(PortfolioItem)
class PortfolioItem(admin.ModelAdmin):

    list_display = ['image_tag']
