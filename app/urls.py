from django.urls import path
from .views import PlotsAPIView

urlpatterns = [
    path('api/v1/plots/', PlotsAPIView.as_view(), name='plots_list'),
    path('api/v1/plots/<int:pk>/', PlotsAPIView.as_view(), name='plot'),
]
