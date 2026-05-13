from django.db import models

class ConfiguracionAgenda(models.Model):
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    duracion_turno = models.IntegerField()

    def generarTurnos(self):
        # Lógica para crear turnos automáticamente
        pass

    def __str__(self):
        return f"Configuración {self.hora_inicio} - {self.hora_fin}"

class Agenda(models.Model):
    fecha = models.DateField()
    activo = models.BooleanField(default=True)
    # Relación "usa" del diagrama
    configuracion = models.ForeignKey(ConfiguracionAgenda, on_delete=models.CASCADE)

    def activarAgenda(self):
        self.activo = True
        self.save()

    def desactivarAgenda(self):
        self.activo = False
        self.save()

    def __str__(self):
        return f"Agenda del {self.fecha}"

class Paciente(models.Model):
    dni = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Turno(models.Model):
    hora = models.TimeField()
    estado = models.CharField(max_length=50, default="Pendiente")
    disponible = models.BooleanField(default=True)
    
    # Relaciones "perteneceA" y "tieneAsignados" del diagrama
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, related_name="turnos")
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True, blank=True, related_name="turnos")

    def reservar(self):
        self.disponible = False
        self.estado = "Reservado"
        self.save()

    def cancelar(self):
        self.disponible = True
        self.estado = "Disponible"
        self.save()

    def atender(self):
        self.estado = "Atendido"
        self.save()