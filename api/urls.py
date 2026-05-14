from django.urls import path
from .views import predict
from .views import predict, home
urlpatterns = [
    path("", home),
    path("predict/", predict),
]