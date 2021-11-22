from django.db import models
from django.db.models.fields.files import ImageField
from django.utils.html import format_html
from apps.shared.models import BaseEntity


class PortfolioItem(BaseEntity):
    image = ImageField(verbose_name="image", upload_to="portfolio/images")

    def image_tag(self):
        print(self.image)
        return format_html('<img src="{}" width="150" height="150" />'.format(self.image.url))


class HomePageSection(BaseEntity):
    title = models.CharField(verbose_name='Título Principal', max_length=100)
    subtitle = models.CharField(
        verbose_name='Título Secundário', max_length=255)


class HomePageContent(BaseEntity):
    sections = models.ManyToManyField(HomePageSection)
