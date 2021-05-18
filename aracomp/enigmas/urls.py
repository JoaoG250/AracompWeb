from django.urls import path

from enigmas import views

urlpatterns = [
    path('enigma/', views.EnigmaView.as_view(), name='enigmas'),
    path('enigma/vencedor/', views.EnigmaVencedorView.as_view(), name='enigmas-vencedor'),
    path('enigma/finalizado/', views.EnigmaFinalizadoView.as_view(), name='enigmas-finalizado'),
    path('enigma/reset/', views.EnigmaReset.as_view(), name='enigmas-reset'),
]
