from django.urls import path

from .views import getMainPage, getBlogDetail

app_name = 'main'

urlpatterns = [
    path('', getMainPage),
    path('<slug:slug>/', getBlogDetail, name='getBlogDetail')
]
