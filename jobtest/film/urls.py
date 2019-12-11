from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('<int:id>/', views.detail, name='detail'),
	path('search/', views.search, name='search'),
	path('register/', views.register, name='register'),
]