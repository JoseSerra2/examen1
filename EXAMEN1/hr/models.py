from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null = True)
    puesto = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    porcentaje_completado = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    
    def __str__(self):
        return self.nombre
    
class Asignacion(models.Model):
    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="empleados")
    fecha_asignacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.empleado} -> {self.Proyecto}"
