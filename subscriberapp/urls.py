from django.urls import path

from subscriberapp.views import SubscriptionView

app_name = 'subscriberapp'

urlpatterns = [
    path('subscriber/', SubscriptionView.as_view(), name='subscriber'),
]
