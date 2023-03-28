from django.urls import path
from . import views
urlpatterns = [
    path('',views.page, name="Home Page"),
    path('browse.html',views.page2 , name="brows"),
    path('details.html',views.page3 ,name="det"),
    path('streams.html',views.page3 ,name="str"),
]