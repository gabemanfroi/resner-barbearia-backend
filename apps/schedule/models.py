from django.db import models
from apps.shared.models import BaseEntity, Service


class Appointment(BaseEntity):
    customer_name = models.CharField(max_length=255, verbose_name='Cliente')
    contact_number = models.CharField(max_length=14)
    services = models.ManyToManyField(Service, verbose_name='Serviços')
    time = models.DateTimeField(verbose_name='Horário')

    def __str__(self):
        return 'Agendamento de ' + self.customer_name

    class Meta:
        verbose_name = 'Agendamento'
