from django.urls import path

from subscriberapp.views import SubscriptionView, SubscriptionListView

app_name = 'subscriberapp'

urlpatterns = [
    path('subscriber/', SubscriptionView.as_view(), name='subscriber'),
    path('list/', SubscriptionListView.as_view(), name='list'),
]
