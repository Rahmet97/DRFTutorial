from django.urls import path

from main.views import UserDetail

urlpatterns = [
    path('user-detail', UserDetail.as_view(), name='UserDetail'),
]
