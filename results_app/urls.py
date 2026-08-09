from django.urls import path

from . import views

app_name = "results"

urlpatterns = [
    path("check-result/", views.check_result, name="check_result"),
]