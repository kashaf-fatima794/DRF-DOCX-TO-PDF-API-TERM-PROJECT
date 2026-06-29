from django.urls import path
from .views import DocumentConvertAPIView

urlpatterns = [
    path('convert/', DocumentConvertAPIView.as_view()),
]