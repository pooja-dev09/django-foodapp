from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
urlpatterns = [
    path('register', csrf_exempt(views.register.as_view()),name='register'),

]