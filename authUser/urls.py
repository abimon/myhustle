from django.urls import path
from .views import SignUpView, SignInView, UserUpdateView,SignOutView,PasswordResetRequest, PasswordResetConfirm

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', SignOutView.as_view(), name='signout'),
    path('update/', UserUpdateView.as_view(), name='update_user'),
    path('request-reset-email/', PasswordResetRequest.as_view(), name='password-reset-request'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(),name='password-reset-confirm'),
]
