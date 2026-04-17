from django.contrib import admin
from django.urls import path, include
from myecommerce.views import home
        

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', home),
    path('', include('myecommerce.urls')),   
]