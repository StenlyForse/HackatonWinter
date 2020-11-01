from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='admin'),
    path('citizens', views.citizens, name='citizens'),
    path('addComment', views.addComment, name='addComment')
]