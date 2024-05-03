from django.urls import path
from foundations.views import CreateView, ListView


urlpatterns = [
    path('create/', CreateView.as_view(), name='create'),
    path('list/', ListView.as_view(), name='list'),
]