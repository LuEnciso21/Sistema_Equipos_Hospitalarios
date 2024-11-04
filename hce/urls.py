from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about' , views.about , name='about'),
    path('patients' , views.patients, name='patients'),
    path('patients/crear' , views.crear, name='crear'),
    path('borrar/<int:id>' , views.borrar, name='borrar'),
    path('patients/editar/<int:id>' , views.editar, name='editar'),
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)