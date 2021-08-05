from django.contrib import admin
from django.urls import path, include

from farm_food_project.farm_food_auth.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('auth/', include('farm_food_project.farm_food_auth.urls')),
    path('profiles/', include('farm_food_project.profiles.urls')),
]
