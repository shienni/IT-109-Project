from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
     path('', views.login_user, name='login'),
     path('main', views.main, name='main'),
     path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
     path('register/', views.RegisterPage, name='register'),

    path('task_create/', views.Taskcreate, name='task_create'),
    path('showtask/<Task_id>', views.ShowTask, name='showtask'),
    path('edit/<Task_id>', views.edit, name='edit'),
    path('deltask/<Task_id>', views.DelTask, name='deltask'),




]
