from django.urls import path
from users.views import UsersViews

urlpatterns = [
    path('record/', UsersViews.as_view(), name="record_user"),
]
