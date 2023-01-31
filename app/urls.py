from django.urls import path
from app.views import Landing


urlpatterns = [
    path("", Landing.as_view(), name="landing-page"),
]
