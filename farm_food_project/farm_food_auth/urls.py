from django.urls import path

from farm_food_project.farm_food_auth.views import SignUpView, SignInView, sign_out

urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', sign_out, name='sign out'),
)