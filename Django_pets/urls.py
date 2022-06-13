
from django.contrib import admin
from django.urls import path
from django.urls import include
from pets import urls as pets_urls
from rest_framework.documentation import include_docs_urls
from pets import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='Pets Api')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', views.ProfileView.as_view()),
    path('api/pets/',include(pets_urls)),
    path('api/pets/create', views.CreatePet.as_view()),
    path('api/pets/(?P<pet_id>\w+)$', views.GetPetById.as_view()),


]
