from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("crops", views.AllCropsView.as_view(), name="crops-page"),
    path("crops/<slug:slug>", views.SingleCropView.as_view(), name="crop-detail-page")
]