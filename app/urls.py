from django.urls import path
from app.views import *

app_name = 'app'

urlpatterns = [
    path('ifelse/', ifelse, name = 'ifelse'),
    path('ifelif/', ifelif, name = 'ifelif'),
    path('nestedif', nestedif, name = 'nestedif'),
    path('forloop/', forloop, name = 'forloop'),
]