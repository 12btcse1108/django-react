from django.urls import path

from . import views

urlpatterns = [
    path('', views.TutorialView.as_view(), name='home'),
]
