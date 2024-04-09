from django.urls import path
from .views import FormClass, ListClass
from . import views

app_name = "toukou"

urlpatterns = [
    path('form/', FormClass.as_view(), name='form'),
    path('list/', ListClass.as_view(), name='list'),
    path("post/", views.post, name="post"),
    path('form/touroku', views.touroku, name='touroku'),
]
