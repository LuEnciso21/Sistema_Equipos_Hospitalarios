from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about', views.about, name='about'),
    path('consultar', views.consultar, name='consultar'),  # Nueva ruta para la vista consultar
    path('patients', views.patients, name='patients'),
    path('patients/crear', views.crear, name='crear'),
    path('borrar/<int:id>/<str:tipo>/', views.borrar, name='borrar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('ingresar_activo/', views.ingresar_activo, name='ingresar_activo'),
    path('equipos', views.equipos, name='equipos'),  
    path('equipos_area/<str:area>/', views.equipos_area, name='equipos_area'),
    path('borrar/<int:id>/<str:tipo>/', views.borrar, name='borrar'),
    path('equipo_detalle/<int:equipo_id>/', views.equipo_detalle, name='equipo_detalle'),
    path('editar_equipo/<int:id>/', views.editar_equipo, name='editar_equipo'),  


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
