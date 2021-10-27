from django.urls import path
from . import views
from .views import RegisterAPI

from knox import views as knox_views
from .views import LoginAPI


urlpatterns = [
	path('', views.api_all, name="api-all"),

	path('register/', RegisterAPI.as_view(), name='register'),
	path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),


	path('todo-list/', views.taskList, name="todo-list"),
	path('todo-single/<int:pk>/', views.taskDetail, name="todo-single"),
	path('todo-create/', views.taskCreate, name="todo-create"),

	path('todo-update/<int:pk>/', views.taskUpdate, name="todo-update"),
	path('todo-delete/<int:pk>/', views.taskDelete, name="todo-delete"),
]
