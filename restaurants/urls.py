from django.urls import path
from restaurants.views import RestaurantViews

urlpatterns = [
    path('restaurants/', RestaurantViews.as_view(), name="restaurants"),
    path('restaurants/<int:id>', RestaurantViews.as_view(), name="restaurant_show")
]
