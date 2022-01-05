from django.urls import include, path
from rest_framework import routers
from .views import *

app_name='crud'

router = routers.DefaultRouter()
router.register(r'students', itemcrud, basename="students")
urlpatterns = [
    path('', include(router.urls))
]