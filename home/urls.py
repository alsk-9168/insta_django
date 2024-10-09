from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path('succ/',views.succ,name='succ')
]
