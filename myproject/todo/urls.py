from django.urls import path
from . import views

urlpatterns = [
    path('hi/',views.sayHi),
    path('all_todo/',views.all_todo),
    path('detail/<int:id>/',views.detail,name='detail'),
]