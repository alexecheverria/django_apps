from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='wvy-home'),
    path('projects/', views.projects, name='wvy-projects'),
    path('create-effect/', views.create_effect, name='wvy-create-effect'),
    path('import-file/', views.import_file, name='wvy-import-file'),
    path('sign-in/', views.sign_in, name='wvy-sign-in'),
    path('sign-out/', views.sign_out, name='wvy-sign-out'),
    path('register/', views.register, name='wvy-register'),
]
