from django.urls import path,include
from .views import SignupView,LoginView,EditView,ProfileList

urlpatterns = [

    path('signup/',SignupView.as_view()),
    path('login/',LoginView.as_view()),
    path('forget/',EditView.as_view()),
    path('profile/',ProfileList.as_view()),
]