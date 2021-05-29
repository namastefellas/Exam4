from django.urls import path
from accounts.views.log import login_view, logout_view, register_view
from accounts.views.profile import UserDetailView


app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create/', register_view, name='create_acc'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user_profile')
]