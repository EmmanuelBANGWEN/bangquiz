from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('', views.home, name='home'),
    path('selectlevel/', views.selectlevel, name='selectlevel'),

    path('start/<int:level_id>/', views.start, name='start'),  # URL avec l'ID du niveau
    path('result/', views.result, name='result'),

    path('community/', views.community, name='community'),

]
