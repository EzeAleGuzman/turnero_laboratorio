from django.contrib import admin
from .models import Paciente, Turno, Agenda, ConfiguracionAgenda

admin.site.register(Paciente)
admin.site.register(Turno)
admin.site.register(Agenda)
admin.site.register(ConfiguracionAgenda)
