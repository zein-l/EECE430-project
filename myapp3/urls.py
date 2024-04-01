from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL, handling unified task actions.
    path('success/', views.success, name='success'),  # Success page URL.
]


