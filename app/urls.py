from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.main_page, name='main_page'),  # Root URL
]