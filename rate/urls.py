from django.urls import path
from rate import views


urlpatterns=[
    path('',views.service,name='service')
]