from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('index', views.index, name='index'),
	# path('index1', views.index1, name='index1'),
	path('add', views.add, name='add'),
	path('delete/<int:todo_id>/', views.delete, name='delete'),
	path('completed/<int:todo_id>/', views.completed, name='completed'),
	path('notcompleted/<int:todo_id>/', views.notcompleted, name='notcompleted'),
	path('lighttheme/<int:tt_id>/', views.lighttheme, name='lighttheme'),
	path('darktheme/<int:tt_id>/', views.darktheme, name='darktheme'),
]