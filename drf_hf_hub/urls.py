""" Microservice URLConf """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_hf_hub.views import TextViewSet, RootAPIView

# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("text", TextViewSet, "txt")

router.APIRootView = RootAPIView

urlpatterns = [
    path("", include(router.urls)),
]
