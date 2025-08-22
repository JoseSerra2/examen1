from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSet, ProyectoViewSet, AsignacionViewSet

router = DefaultRouter()
router.register(r'empleados', EmpleadoViewSet)
router.register(r'proyectos', ProyectoViewSet)
router.register(r'asignaciones', AsignacionViewSet)

urlpatterns = router.urls
