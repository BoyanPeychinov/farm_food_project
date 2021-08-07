from django.urls import path

from farm_food_project.profiles.views import ListProducersProfilesView, ProducerProfileDetailsView

urlpatterns = (
    path('', ListProducersProfilesView.as_view(), name='list producers'),
    path('details/<int:pk>', ProducerProfileDetailsView.as_view(), name='producer detail'),
)