from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', pelayanan, name='pelayanan'),
    path('pelayanan/update', views.updateStatus, name="updatestatus"),
    path('pelayanan/filter/', views.filterpelayanan, name='filterpelayanan'),
    path('editstatus/<str:pk>/', views.editstatus, name='editstatus'),
    path('detailpelayanan/<str:pk>/', views.detailpelayanan, name='detailpelayanan'),
    path('detaildaftar/<str:pk>/', views.detaildaftar, name='detaildaftar'),
    path('<str:pk>/delete', views.deletepelayanan, name='deletepelayanan'),
    path('pelayanan/pelayanandel/<str:pk>/', views.pelayanandel, name='pelayanandel'),
]
