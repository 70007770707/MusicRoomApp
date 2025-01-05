from django.urls import path
from .views import index

# is used in the return method in backend /spodify/views.py
app_name = 'frontend'

urlpatterns = [
    path('', index, name=''),
    path('join', index),
    path('create', index),
    path('room/<str:roomCode>', index),
    path('info', index)
]