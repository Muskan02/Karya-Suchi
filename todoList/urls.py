from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('index1', views.index1, name='index1'),
	path('add', views.add, name='add'),
	path('delete/<int:todo_id>/', views.delete, name='delete')
]