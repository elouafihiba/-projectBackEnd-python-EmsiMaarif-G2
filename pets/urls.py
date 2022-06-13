
from django.urls import path
from pets import views
from django.urls import path, include
from .views import (
    ListPetsAPIView,
    # PetDetailApiView
)


urlpatterns = [
    path('', ListPetsAPIView.as_view()),
    # path('<int:pet_id>/', ListPetsAPIView.as_view()),

]
