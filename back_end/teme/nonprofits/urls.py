
from django.urls import path
from nonprofits.views import CreateView, ListView, SentMailsListView, SendMailView


urlpatterns = [
    path('create/', CreateView.as_view()),
    path('list/', ListView.as_view()),
    path('sent-mails/', SentMailsListView.as_view()),
    path('send-mail/', SendMailView.as_view()),
]