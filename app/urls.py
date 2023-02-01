from django.urls import path
from app.views import Landing, LogIn, Dashboard


urlpatterns = [
    path("", Landing.as_view(), name="landing-page"),
    path("login/", LogIn.as_view(), name="login"),

    path("dashboard/", Dashboard.as_view(), name="dashboard"),
]
