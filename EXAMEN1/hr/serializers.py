from rest_framework import serializers
from .models import Empleado, Proyecto, Asignacion

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'
        
class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'
        
class AsignacionSerializer(serializers.ModelSerializer):
    empleado = EmpleadoSerializer(read_only = True)
    empleado_id = serializers.PrimaryKeyRelatedField(queryset = Empleado.objects.all(), source="empleado", write_only = True)
    proyecto = ProyectoSerializer(read_only=True)
    proyecto_id = serializers.PrimaryKeyRelatedField(queryset = Proyecto.objects.all(), source="proyecto", write_only = True)
    
    class Meta:
        model = Asignacion
        fields = ['id', 'empleado', 'empleado_id', 'proyecto', 'proyecto_id', 'fecha_asignacion']