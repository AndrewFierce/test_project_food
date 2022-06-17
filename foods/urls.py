from rest_framework.routers import re_path
from .views import FoodListViewSet

urlpatterns = [
    re_path(r"^$", FoodListViewSet.as_view(), name="food-list"),
]