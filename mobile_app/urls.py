from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Store, name="Store"),
    path('login/', views.Login, name="Login"),
    path('register/', views.Register, name="Register"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
