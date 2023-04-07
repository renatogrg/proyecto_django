 
from django.urls import path  
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.mi_vista),
    path('mostrar-fecha/', views.mostrar_fecha),
    path('saludar/<str:nombre>/<str:apellido>/', views.saludar),
    path('mi-primer-template/', views.mi_primer_template),
    path('prueba-template/', views.prueba_template),
    path('prueba-render/', views.prueba_render),
    
    
]