from django.urls import path

from farm_food_project.profiles.views import ListProducersProfilesView, ProducerProfileDetailsView, \
    ConsumerProfileDetailsView, ProducerDetailsFromListView

urlpatterns = (
    path('', ListProducersProfilesView.as_view(), name='list producers'),
    path('producer-details/', ProducerProfileDetailsView.as_view(), name='producer details'),
    path('farm-details/<int:pk>', ProducerDetailsFromListView.as_view(), name='farm details'),
    path('customer-details/', ConsumerProfileDetailsView.as_view(), name='consumer detail'),
)