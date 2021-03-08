from django.urls import path
from users.views import signin_view, signout_view, signup_view

urlpatterns = [
    path('account/criar/', signup_view, name='signup'),
    path('account/logar/', signin_view, name='signin'),
    path('account/deslogar/', signout_view, name='signout'),
]