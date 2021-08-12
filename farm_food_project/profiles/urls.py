from django.urls import path

from farm_food_project.profiles.views import ListProducersProfilesView, ProducerProfileDetailsView, \
    ConsumerProfileDetailsView, ProducerDetailsFromListView, EditProducerProfileView, EditConsumerProfileView

urlpatterns = (
    path('', ListProducersProfilesView.as_view(), name='list producers'),
    path('producer-details/', ProducerProfileDetailsView.as_view(), name='producer details'),
    path('edit-producer/<int:pk>', EditProducerProfileView.as_view(), name='edit producer'),
    path('farm-details/<int:pk>', ProducerDetailsFromListView.as_view(), name='farm details'),
    path('consumer-details/', ConsumerProfileDetailsView.as_view(), name='consumer detail'),
    path('edit-consumer/<int:pk>', EditConsumerProfileView.as_view(), name='edit consumer'),

)