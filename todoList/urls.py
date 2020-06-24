from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('index', views.index, name='index'),
	path('signup', views.signup, name='signup'),
	path('signin', views.signin, name='signin'),
	path('signout', views.signout, name='signout'),
	path('welcome', views.welcome, name='welcome'),
	path('add', views.add, name='add'),
	path('delete/<int:todo_id>/', views.delete, name='delete'),
	path('completed/<int:todo_id>/', views.completed, name='completed'),
	path('notcompleted/<int:todo_id>/', views.notcompleted, name='notcompleted'),
	path('lighttheme/<int:tt_id>/', views.lighttheme, name='lighttheme'),
	path('darktheme/<int:tt_id>/', views.darktheme, name='darktheme'),
]