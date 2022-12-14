from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('records/', views.records_index, name='index'),
  path('records/<int:records_id>',views.records_detail, name "detail"),
]