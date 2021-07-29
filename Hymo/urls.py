from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    #path('login/', views.login, name='login'),
    path('details/', views.details, name='details'),
    path('add/', views.adddoctor, name='add'),
    path('<int:id>/edit/', views.editdoctor, name='edit'),
    path('<int:id>/delete/', views.delete, name='delete'),

]