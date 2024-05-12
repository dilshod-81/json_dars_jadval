from django.urls import path

from .views import summu_dars_jadval


urlpatterns = [
    path('', summu_dars_jadval, name='summu_dars_jadval'),
]