from django.urls import path
from users import views

urlpatterns = [
    path('signup/', views.UserSignUpView.as_view(),),
]