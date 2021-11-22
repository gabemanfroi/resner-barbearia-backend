from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AppointmentSerializer
from .models import Appointment


class AppointViewSet(viewsets.ModelViewSet):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
