from django.contrib import admin
from django.urls import path
from django.urls import include
from foundations import urls


urlpatterns = [
    path('foundations/', include('foundations.urls')),
    path('nonprofits/', include('nonprofits.urls'))
]