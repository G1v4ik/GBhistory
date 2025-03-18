from django.urls import path
from .views import index as index_view\


urlpatterns = [
    path('', index_view ,name='home'),
]