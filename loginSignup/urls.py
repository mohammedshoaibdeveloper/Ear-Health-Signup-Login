from django.urls import path,include
from .views import SignupView,LoginView,EditView

urlpatterns = [

    path('signup/',SignupView.as_view()),
    path('login/',LoginView.as_view()),
    path('forget/',EditView.as_view()),
]