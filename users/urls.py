from django.urls import path
from . views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('show/', ShowDetails.as_view(), name='ShowDetails'),
    path('delete-user/', DeleteUser.as_view(), name='delete-user'),
    path('edit-user/<int:id>/', EditUser.as_view(), name='edit-user'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout')
]