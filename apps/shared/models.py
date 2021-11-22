from django.db import models

class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self)-> str:
        return self + ' is added.'

    class Meta:
        abstract = True

class Service(BaseEntity):
    title = models.CharField(verbose_name = 'Título',max_length=100)
    price = models.DecimalField(verbose_name='Preço',decimal_places=2, max_digits=7)
    estimated_time = models.TimeField(verbose_name = 'Tempo Estimado')

    def __str__(self) -> str:
        return self.title
