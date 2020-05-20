from django.urls import path, include
from .views import SignUpView, AccountView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('account/', AccountView.as_view(), name='account'),
]
