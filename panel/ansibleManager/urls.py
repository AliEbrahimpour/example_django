from django.urls import path
from . import views

urlpatterns = [
#     path('all_todo/',views.all_todo),
    path('', views.home, name='home'),
    path('detail/<int:id>/', views.detail, name='detail'),

]