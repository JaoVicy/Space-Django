from django.urls import path
from galeria.views import index, imagem


urlpatterns = [
    path('', index),
    path('imagem/', imagem, name = 'imagem'),  # Assuming you want to handle 'imagem' view as well
]